	.file	"code.c"
 # GNU C11 (tdm64-1) version 5.1.0 (x86_64-w64-mingw32)
 #	compiled by GNU C version 5.1.0, GMP version 4.3.2, MPFR version 2.4.2, MPC version 0.8.2
 # GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
 # options passed: 
 # -iprefix C:/TDM-GCC-64/bin/../lib/gcc/x86_64-w64-mingw32/5.1.0/
 # -D_REENTRANT code.c -mtune=generic -march=x86-64
 # -auxbase-strip code-O0.s -O0 -Wall -fverbose-asm -fdump-tree-all
 # options enabled:  -faggressive-loop-optimizations
 # -fasynchronous-unwind-tables -fauto-inc-dec -fchkp-check-incomplete-type
 # -fchkp-check-read -fchkp-check-write -fchkp-instrument-calls
 # -fchkp-narrow-bounds -fchkp-optimize -fchkp-store-bounds
 # -fchkp-use-static-bounds -fchkp-use-static-const-bounds
 # -fchkp-use-wrappers -fcommon -fdelete-null-pointer-checks
 # -fdwarf2-cfi-asm -fearly-inlining -feliminate-unused-debug-types
 # -ffunction-cse -fgcse-lm -fgnu-runtime -fgnu-unique -fident
 # -finline-atomics -fira-hoist-pressure -fira-share-save-slots
 # -fira-share-spill-slots -fivopts -fkeep-inline-dllexport
 # -fkeep-static-consts -fleading-underscore -flifetime-dse
 # -flto-odr-type-merging -fmath-errno -fmerge-debug-strings -fpeephole
 # -fpic -fprefetch-loop-arrays -freg-struct-return
 # -fsched-critical-path-heuristic -fsched-dep-count-heuristic
 # -fsched-group-heuristic -fsched-interblock -fsched-last-insn-heuristic
 # -fsched-rank-heuristic -fsched-spec -fsched-spec-insn-heuristic
 # -fsched-stalled-insns-dep -fschedule-fusion -fsemantic-interposition
 # -fset-stack-executable -fshow-column -fsigned-zeros
 # -fsplit-ivs-in-unroller -fstdarg-opt -fstrict-volatile-bitfields
 # -fsync-libcalls -ftrapping-math -ftree-coalesce-vars -ftree-cselim
 # -ftree-forwprop -ftree-loop-if-convert -ftree-loop-im
 # -ftree-loop-ivcanon -ftree-loop-optimize -ftree-parallelize-loops=
 # -ftree-phiprop -ftree-reassoc -ftree-scev-cprop -funit-at-a-time
 # -funwind-tables -fverbose-asm -fzero-initialized-in-bss
 # -m128bit-long-double -m64 -m80387 -maccumulate-outgoing-args
 # -malign-double -malign-stringops -mavx256-split-unaligned-load
 # -mavx256-split-unaligned-store -mfancy-math-387 -mfentry -mfp-ret-in-387
 # -mfxsr -mieee-fp -mlong-double-80 -mmmx -mms-bitfields -mno-sse4
 # -mpush-args -mred-zone -msse -msse2 -mstack-arg-probe -mvzeroupper

	.text
	.globl	foo
	.def	foo;	.scl	2;	.type	32;	.endef
	.seh_proc	foo
foo:
	pushq	%rbp	 #
	.seh_pushreg	%rbp
	movq	%rsp, %rbp	 #,
	.seh_setframe	%rbp, 0
	.seh_endprologue
	movl	%ecx, 16(%rbp)	 # a, a
	movq	%rdx, 24(%rbp)	 # b, b
	movq	24(%rbp), %rax	 # b, tmp90
	movl	(%rax), %edx	 # *b_2(D), D.2593
	movl	16(%rbp), %eax	 # a, tmp91
	addl	%edx, %eax	 # D.2593, D.2593
	popq	%rbp	 #
	ret
	.seh_endproc
	.section .rdata,"dr"
.LC0:
	.ascii "%d\12\0"
	.text
	.globl	func
	.def	func;	.scl	2;	.type	32;	.endef
	.seh_proc	func
func:
	pushq	%rbp	 #
	.seh_pushreg	%rbp
	movq	%rsp, %rbp	 #,
	.seh_setframe	%rbp, 0
	subq	$48, %rsp	 #,
	.seh_stackalloc	48
	.seh_endprologue
	movl	$7, -8(%rbp)	 #, y
	movq	.refptr.x(%rip), %rax	 #, tmp88
	movl	(%rax), %eax	 # x, D.2594
	leaq	-8(%rbp), %rdx	 #, tmp89
	movl	%eax, %ecx	 # D.2594,
	call	foo	 #
	movl	%eax, -4(%rbp)	 # tmp90, r
	movl	-4(%rbp), %eax	 # r, tmp91
	movl	%eax, %edx	 # tmp91,
	leaq	.LC0(%rip), %rcx	 #,
	call	printf	 #
	nop
	addq	$48, %rsp	 #,
	popq	%rbp	 #
	ret
	.seh_endproc
	.def	__main;	.scl	2;	.type	32;	.endef
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
	pushq	%rbp	 #
	.seh_pushreg	%rbp
	movq	%rsp, %rbp	 #,
	.seh_setframe	%rbp, 0
	subq	$32, %rsp	 #,
	.seh_stackalloc	32
	.seh_endprologue
	call	__main	 #
	call	func	 #
	movl	$0, %eax	 #, D.2597
	addq	$32, %rsp	 #,
	popq	%rbp	 #
	ret
	.seh_endproc
	.ident	"GCC: (tdm64-1) 5.1.0"
	.def	printf;	.scl	2;	.type	32;	.endef
	.section	.rdata$.refptr.x, "dr"
	.globl	.refptr.x
	.linkonce	discard
.refptr.x:
	.quad	x
