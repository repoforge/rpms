# $Id$
# Authority: yury
# Upstream: David Mansfield <cvsps$dm,cobite,com>

### EL6 ships with cvsps-2.2-0.6.b1.el6
# ExclusiveDist: el2 el3 el4 el5

Summary: Patchset tool for CVS
Name: cvsps
Version: 2.1
Release: 6%{?dist}
Group: Development/Tools
License: GPL
URL: http://www.cobite.com/cvsps/

Source0: http://www.cobite.com/cvsps/%{name}-%{version}.tar.gz
Patch0: cvsps-2.1-cflags.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel
# Requires cvs only with --no-cvs-direct, but I cannot imagine this dep
# being a problem on systems where cvsps will be installed...
Requires: cvs

%description
CVSps is a program for generating 'patchset' information from a CVS
repository.  A patchset in this case is defined as a set of changes
made to a collection of files, and all committed at the same time
(using a single 'cvs commit' command).  This information is valuable
to seeing the big picture of the evolution of a cvs project.  While
cvs tracks revision information, it is often difficult to see what
changes were committed 'atomically' to the repository.

%prep
%setup
%patch0 -p1 -b .cflags

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 cvsps $RPM_BUILD_ROOT%{_bindir}/cvsps
install -Dpm 644 cvsps.1 $RPM_BUILD_ROOT%{_mandir}/man1/cvsps.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGELOG COPYING README merge_utils.sh
%{_bindir}/cvsps
%{_mandir}/man1/cvsps.1*

%changelog
* Wed Sep 22 2010 Yury V. Zaytsev <yury@shurup.com> - 2.1-6
- Fixed build failure due to the incompatibility with DAR.

* Tue Dec  8 2009 Yury V. Zaytsev <yury@shurup.com> - 2.1-5
- Ported over RPMForge from EPEL with minor updates.

* Tue Aug 29 2006 Ville Skyttä <ville.skytta at iki.fi> - 2.1-4
- Rebuild.

* Wed Feb 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 2.1-3
- Rebuild.

* Fri May 27 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.1-2
- 2.1.

* Sun Mar 20 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.0-0.2.rc1
- Drop 0.fdr and Epoch: 0.

* Sun Sep 14 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.0-0.fdr.0.2.rc1
- Remove #---- section markers.

* Fri Jul  4 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.0-0.fdr.0.1.rc1
- First build.
