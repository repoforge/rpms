# $Id$
# Authority: dag

Summary: Control process scheduler attributres and CPU affinity
Name: run
Version: 3.0
Release: 2
License: GPL
Group: Applications/System
URL: http://www.ccur.com/id_oss.asp

Source: http://www.ccur.com/oss/run-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf, automake

%description
Set scheduling parameters and CPU bias for a new process or a
list of existing processes/threads.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
#libtool --finish %{buildroot}%{_libdir}

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING LICENSE NEWS README
%doc %{_mandir}/man1/run.1*
%doc %{_mandir}/man3/mpadvise.3*
%doc %{_mandir}/man3/cpuset.3*
%{_bindir}/run
%{_libdir}/libmpadvise.*
%{_includedir}/cpuset.h
%{_includedir}/mpadvise.h
%{_includedir}/proc_walk.h
%{_includedir}/proc_stat.h

%changelog
* Thu Sep 30 2004 Dag Wieers <dag@wieers.com> - 3.0-2
- Fixed misplaced %Mdefattr. (Truls Gulbrandsen)

* Wed Sep 29 2004 Dag Wieers <dag@wieers.com> - 3.0-1
- Initial package. (using DAR)
