	.file	"code2.c"
 # GNU C11 (tdm64-1) version 5.1.0 (x86_64-w64-mingw32)
 #	compiled by GNU C version 5.1.0, GMP version 4.3.2, MPFR version 2.4.2, MPC version 0.8.2
 # GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
 # options passed: 
 # -iprefix C:/TDM-GCC-64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.0/
 # -D_REENTRANT code2.c -mtune=generic -march=x86-64
 # -auxbase-strip code2-O2.s -O2 -Wall -fverbose-asm -fdump-tree-all
 # options enabled:  -faggressive-loop-optimizations -falign-labels
 # -fasynchronous-unwind-tables -fauto-inc-dec -fbranch-count-reg
 # -fcaller-saves -fchkp-check-incomplete-type -fchkp-check-read
 # -fchkp-check-write -fchkp-instrument-calls -fchkp-narrow-bounds
 # -fchkp-optimize -fchkp-store-bounds -fchkp-use-static-bounds
 # -fchkp-use-static-const-bounds -fchkp-use-wrappers
 # -fcombine-stack-adjustments -fcommon -fcompare-elim -fcprop-registers
 # -fcrossjumping -fcse-follow-jumps -fdefer-pop
 # -fdelete-null-pointer-checks -fdevirtualize -fdevirtualize-speculatively
 # -fdwarf2-cfi-asm -fearly-inlining -feliminate-unused-debug-types
 # -fexpensive-optimizations -fforward-propagate -ffunction-cse -fgcse
 # -fgcse-lm -fgnu-runtime -fgnu-unique -fguess-branch-probability
 # -fhoist-adjacent-loads -fident -fif-conversion -fif-conversion2
 # -findirect-inlining -finline -finline-atomics
 # -finline-functions-called-once -finline-small-functions -fipa-cp
 # -fipa-cp-alignment -fipa-icf -fipa-icf-functions -fipa-icf-variables
 # -fipa-profile -fipa-pure-const -fipa-ra -fipa-reference -fipa-sra
 # -fira-hoist-pressure -fira-share-save-slots -fira-share-spill-slots
 # -fisolate-erroneous-paths-dereference -fivopts -fkeep-inline-dllexport
 # -fkeep-static-consts -fleading-underscore -flifetime-dse -flra-remat
 # -flto-odr-type-merging -fmath-errno -fmerge-constants
 # -fmerge-debug-strings -fmove-loop-invariants -fomit-frame-pointer
 # -foptimize-sibling-calls -foptimize-strlen -fpartial-inlining -fpeephole
 # -fpeephole2 -fpic -fprefetch-loop-arrays -free -freg-struct-return
 # -freorder-blocks -freorder-blocks-and-partition -freorder-functions
 # -frerun-cse-after-loop -fsched-critical-path-heuristic
 # -fsched-dep-count-heuristic -fsched-group-heuristic -fsched-interblock
 # -fsched-last-insn-heuristic -fsched-rank-heuristic -fsched-spec
 # -fsched-spec-insn-heuristic -fsched-stalled-insns-dep -fschedule-fusion
 # -fschedule-insns2 -fsemantic-interposition -fset-stack-executable
 # -fshow-column -fshrink-wrap -fsigned-zeros -fsplit-ivs-in-unroller
 # -fsplit-wide-types -fssa-phiopt -fstdarg-opt -fstrict-aliasing
 # -fstrict-overflow -fstrict-volatile-bitfields -fsync-libcalls
 # -fthread-jumps -ftoplevel-reorder -ftrapping-math -ftree-bit-ccp
 # -ftree-builtin-call-dce -ftree-ccp -ftree-ch -ftree-coalesce-vars
 # -ftree-copy-prop -ftree-copyrename -ftree-cselim -ftree-dce
 # -ftree-dominator-opts -ftree-dse -ftree-forwprop -ftree-fre
 # -ftree-loop-if-convert -ftree-loop-im -ftree-loop-ivcanon
 # -ftree-loop-optimize -ftree-parallelize-loops= -ftree-phiprop -ftree-pre
 # -ftree-pta -ftree-reassoc -ftree-scev-cprop -ftree-sink -ftree-slsr
 # -ftree-sra -ftree-switch-conversion -ftree-tail-merge -ftree-ter
 # -ftree-vrp -funit-at-a-time -funwind-tables -fverbose-asm
 # -fzero-initialized-in-bss -m128bit-long-double -m64 -m80387
 # -maccumulate-outgoing-args -malign-double -malign-stringops
 # -mavx256-split-unaligned-load -mavx256-split-unaligned-store
 # -mfancy-math-387 -mfentry -mfp-ret-in-387 -mfxsr -mieee-fp
 # -mlong-double-80 -mmmx -mms-bitfields -mno-sse4 -mpush-args -mred-zone
 # -msse -msse2 -mstack-arg-probe -mvzeroupper

	.section .rdata,"dr"
.LC0:
	.ascii "%d\12\0"
	.section	.text.unlikely,"x"
.LCOLDB1:
	.text
.LHOTB1:
	.p2align 4,,15
	.globl	func
	.def	func;	.scl	2;	.type	32;	.endef
	.seh_proc	func
func:
	.seh_endprologue
	movq	.refptr.x(%rip), %rax	 #, tmp89
	leaq	.LC0(%rip), %rcx	 #,
	movl	(%rax), %edx	 # x, x
	addl	$7, %edx	 #, r
	jmp	printf	 #
	.seh_endproc
	.section	.text.unlikely,"x"
.LCOLDE1:
	.text
.LHOTE1:
	.def	__main;	.scl	2;	.type	32;	.endef
	.section	.text.unlikely,"x"
.LCOLDB2:
	.section	.text.startup,"x"
.LHOTB2:
	.p2align 4,,15
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
	subq	$40, %rsp	 #,
	.seh_stackalloc	40
	.seh_endprologue
	call	__main	 #
	movq	.refptr.x(%rip), %rax	 #, tmp90
	leaq	.LC0(%rip), %rcx	 #,
	movl	(%rax), %edx	 # x, x
	addl	$7, %edx	 #, r
	call	printf	 #
	xorl	%eax, %eax	 #
	addq	$40, %rsp	 #,
	ret
	.seh_endproc
	.section	.text.unlikely,"x"
.LCOLDE2:
	.section	.text.startup,"x"
.LHOTE2:
	.ident	"GCC: (tdm64-1) 5.1.0"
	.def	printf;	.scl	2;	.type	32;	.endef
	.section	.rdata$.refptr.x, "dr"
	.globl	.refptr.x
	.linkonce	discard
.refptr.x:
	.quad	x
