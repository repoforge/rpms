# $Id$
# Authority: dag

# ExclusiveDist: el6

%define	with_python		--with-python
%define	with_python_version	%(echo `python -c "import sys; print sys.version[:3]"`)
#define with_java		--with-java

Summary: An open source cryptography library.
Name: beecrypt
Version: 4.1.2
Release: 10.1.1%{?dist}
Group: System Environment/Libraries
License: LGPL
URL: http://sourceforge.net/projects/beecrypt
Source0: http://prdownloads.sourceforge.net/beecrypt/%{name}-%{version}.tar.gz
Source1: http://prdownloads.sourceforge.net/beecrypt/%{name}-%{version}.tar.gz.sig
Patch0: beecrypt-4.1.2-base64.patch
Patch1: beecrypt-4.1.2-python-api.patch
Patch2: beecrypt-4.1.2-biarch.patch
BuildPreReq: doxygen tetex-dvips tetex-latex
BuildRequires: m4
%if %{?with_python:1}0
BuildPreReq: python-devel >= %{with_python_version}
%endif
BuildRoot: %{_tmppath}/%{name}-root
Obsoletes: beecrypt-java =< 4.1.2-2

%description
Beecrypt is a general-purpose cryptography library.

%package devel
Summary: Files needed for developing applications with beecrypt.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Beecrypt is a general-purpose cryptography library.  This package contains
files needed for developing applications with beecrypt.

%if %{?with_python:1}0
%package python
Summary: Files needed for python applications using beecrypt.
Group: Development/Libraries
Requires: python >= %{with_python_version}
Requires: %{name} = %{version}-%{release}

%description python
Beecrypt is a general-purpose cryptography library.  This package contains
files needed for using python with beecrypt.
%endif

%if %{?with_java:1}0
%package java
Summary: Files needed for java applications using beecrypt.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description java
Beecrypt is a general-purpose cryptography library.  This package contains
files needed for using java with beecrypt.
%endif

%prep
%setup -q
%patch0 -p1 -b .base64
%patch1 -p1 -b .python-api
%patch2 -p1 -b .biarch

%build

%configure --enable-shared --enable-static %{?with_python} \
    %{?with_java}%{!?with_java:--with-java=no} --with-cplusplus=no

make %{?_smp_mflags} \
	%{?with_python:pythondir="%{_libdir}/python%{with_python_version}/site-packages"}
doxygen

%install
rm -fr $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT \
  %{?with_python:pythondir="%{_libdir}/python%{with_python_version}/site-packages"}

# XXX nuke unpackaged files, artifacts from using libtool to produce module
rm -f ${RPM_BUILD_ROOT}%{_libdir}/python%{with_python_version}/site-packages/_bc.*a

# XXX delete next line to build with legacy, non-check aware, rpmbuild.
%check
make check || :
cat /proc/cpuinfo
make bench || :

%clean
rm -fr $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README BENCHMARKS
%{_libdir}/libbeecrypt.so.*

%files devel
%defattr(-,root,root)
%doc BUGS
%{_includedir}/%{name}
%{_libdir}/libbeecrypt.a
%{_libdir}/libbeecrypt.la
%{_libdir}/libbeecrypt.so

%if %{?with_python:1}0
%files python
%defattr(-,root,root)
%{_libdir}/python%{with_python_version}/site-packages/_bc.so
%endif

%if %{?with_java:1}0
%files java
%defattr(-,root,root)
%{_libdir}/libbeecrypt_java.a
%{_libdir}/libbeecrypt_java.la
%{_libdir}/libbeecrypt_java.so*
%endif

%changelog
* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 4.1.2-10.1.1
- rebuild

* Tue Jun 27 2006 Paul Nasrat <pnasrat@redhat.com> - 4.1.2-10.1
- Fix missing BR

* Mon May 22 2006 Paul Nasrat <pnasrat@redhat.com> - 4.1.2-10
- Make multilib-devel work

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 4.1.2-9.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 4.1.2-9.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Oct 15 2005 Florian La Roche <laroche@redhat.com>
- Use -with-cplusplus=no. The libs still require libstdc++, so
  this needs further cleanup.

* Tue May 17 2005 Miloslav Trmac <mitr@redhat.com> - 4.1.2-8
- Remove dependencies on private symbols not present in Python 2.4 from
  beecrypt-python

* Tue May 17 2005 Miloslav Trmac <mitr@redhat.com> - 4.1.2-7
- Doh, actually apply the patch

* Tue May 17 2005 Miloslav Trmac <mitr@redhat.com> - 4.1.2-6
- Fix b64encode() for data starting with NUL (#123650)

* Fri Apr 01 2005 Warren Togami <wtogami@redhat.com> 4.1.2-5
- remove huge API docs

* Fri Apr 01 2005 Paul Nasrat <pnasrat@redhat.com> 4.1.2-4
- Obsolete older beecrypt-java

* Tue Mar 29 2005 Paul Nasrat <pnasrat@redhat.com> 4.1.2-3
- Disable beecrypt-java (#151294)

* Fri Mar  4 2005 Jeff Johnson <jbj@redhat.com> 4.1.2-2
- rebuild with gcc4.

* Sat Feb  5 2005 Jeff Johnson <jbj@jbj.org> 4.1.2-1
- upgrade to 4.1.2
- put java components in sub-package.
- check that /usr/lib64 is not used on alpha (#146583).

* Fri Feb  4 2005 Miloslav Trmac <mitr@redhat.com> - 3.1.0-7
- Rebuild against Python 2.4

* Sun Aug 08 2004 Alan Cox <alan@redhat.com> 3.1.0-6
- Build requires libtool (Steve Grubb)

* Fri Jul 02 2004 Elliot Lee <sopwith@redhat.com> 3.1.0-5
- rebuilt
- Add _smp_mflags

* Wed Mar 24 2004 Jeff Johnson <jbj@redhat.com> 3.1.0-3
- fix: extgcd_w problem fixed by upgrading from CVS.

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Dec 22 2003 Jeff Johnson <jbj@jbj.org> 3.1.0-1
- upgrade to 3.1.0.
- recompile against python-2.3.3.

* Mon Jun 30 2003 Jeff Johnson <jbj@redhat.com> 3.0.1-0.20030630
- upstream fixes for DSA and ppc64.

* Mon Jun 23 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-2
- upgrade to 3.0.0 final.
- fix for DSA (actually, modulo inverse) sometimes failing.

* Fri Jun 20 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-1.20030619
- avoid asm borkage on ppc64.

* Thu Jun 19 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-1.20030618
- rebuild for release bump.

* Tue Jun 17 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-1.20030616
- try to out smart libtool a different way.
- use $bc_target_cpu, not $bc_target_arch, to detect /usr/lib64.

* Mon Jun 16 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-1.20030615
- use -mcpu=powerpc64 on ppc64.

* Fri Jun 13 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-1.20030613
- upgrade to latest snapshot.

* Fri Jun  6 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-1.20030605
- rebuild into another tree.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-0.20030603
- update to 3.0.0 snapshot, fix mpmod (and DSA) on 64b platforms.

* Mon Jun  2 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-0.20030602
- update to 3.0.0 snapshot, merge patches, fix gcd rshift and ppc problems.

* Thu May 29 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-0.20030529
- update to 3.0.0 snapshot, fix ia64/x86_64 build problems.

* Wed May 28 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-0.20030528
- upgrade to 3.0.0 snapshot, adding rpm specific base64.[ch] changes.
- add PYTHONPATH=.. so that "make check" can test the just built _bc.so module.
- grab cpuinfo and run "make bench".
- continue ignoring "make check" failures, LD_LIBRARY_PATH needed for _bc.so.
- skip asm build failure on ia64 for now.
- ignore "make bench" exit codes too, x86_64 has AES segfault.

* Wed May 21 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-0.20030521
- upgrade to 3.0.0 snapshot, including python subpackage.
- ignore "make check" failure for now.

* Fri May 16 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-0.20030516
- upgrade to 3.0.0 snapshot, including ia64 and x86_64 fixes.
- add %%check.
- ignore "make check" failure on ia64 for now.

* Mon May 12 2003 Jeff Johnson <jbj@redhat.com> 3.0.0-0.20030512
- upgrade to 3.0.0 snapshot.
- add doxygen doco.
- use /dev/urandom as default entropy source.
- avoid known broken compilation for now.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Nov 19 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches

* Fri Aug  2 2002 Jeff Johnson <jbj@redhat.com> 2.2.0-6
- install types.h (#68999).

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun  5 2002 Jeff Johnson <jbj@redhat.com>
- run ldconfig when installing/erasing (#65974).

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May 13 2002 Jeff Johnson <jbj@redhat.com>
- upgrade to latest 2.2.0 (from cvs.rpm.org).

* Mon Jan 21 2002 Jeff Johnson <jbj@redhat.com>
- use the same beecrypt-2.2.0 that rpm is using internally.

* Thu Jan 10 2002 Nalin Dahyabhai <nalin@redhat.com> 2.1.0-1
- initial package
