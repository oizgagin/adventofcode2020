package main

import (
	"container/list"
	"fmt"
)

func main() {
	m := make(map[uint64]*list.Element)

	l := list.New()
	for _, v := range []uint64{7, 1, 6, 8, 9, 2, 5, 4, 3} {
		m[v] = l.PushBack(uint64(v))
	}
	for i := 10; i <= 1e6; i++ {
		m[uint64(i)] = l.PushBack(uint64(i))
	}

	next := func(n *list.Element) *list.Element {
		v := n.Next()
		if v == nil {
			return l.Front()
		}
		return v
	}

	var taken [3]*list.Element
	takenVals := make([]bool, 1e6+1)

	curr := l.Front()
	for step := 0; step < 1e7; step++ {
		// pick next 3 cups
		p := curr
		for i := 0; i < 3; i++ {
			p = next(p)
			taken[i] = p
			takenVals[p.Value.(uint64)] = true
		}

		// find next dest value
		currVal := curr.Value.(uint64)

		dstVal := currVal - 1
		for dstVal > 0 && takenVals[dstVal] {
			dstVal--
		}
		if dstVal == 0 {
			dstVal = 1e6
			for takenVals[dstVal] {
				dstVal--
			}
		}

		// insert 3 taken cups after dest
		dst := m[dstVal]

		for i := 0; i < 3; i++ {
			l.MoveAfter(taken[i], dst)
			dst = taken[i]
			takenVals[taken[i].Value.(uint64)] = false
		}

		curr = next(curr)
	}

	oneNext := next(m[1])
	oneNextNext := next(oneNext)

	fmt.Println(oneNext.Value.(uint64) * oneNextNext.Value.(uint64))
}
