# $Id$
# Authority: dag

%define real_name ladspa_sdk

Summary: Linux Audio Developer's Simple Plugin API
Name: ladspa
Version: 1.12
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://www.ladspa.org/
Source: http://www.ladspa.org/download/ladspa_sdk_%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Obsoletes: ladspa-sdk <= %{version}-1

%description
There is a large number of synthesis packages in use or development on
the Linux platform at this time. The Linux Audio Developer's Simple
Plugin API (LADSPA) attempts to give programmers the ability to write
simple `plugin' audio processors in C/C++ and link them dynamically
against a range of host applications.


%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.


%prep
%setup -n %{real_name}

### FIXME: Correct URLs to link to local file. (Please fix upstream)
%{__perl} -pi -e 's|HREF="ladspa.h.txt"|HREF="file:///usr/include/ladspa.h"|' doc/*.html

### FIXME: Make Makefile use autotool directory standard (Please fix upstream)
%{__perl} -pi -e '
		s|/usr/local/lib/|\$(libdir)/|;
		s|/usr/include/|\$(includedir)/|;
		s|/usr/local/bin/|\$(bindir)/|;
	' src/makefile

%build
%{__make} %{?_smp_mflags} -C src targets

%install
%{__rm} -rf %{buildroot}
### FIXME: Makefile doesn't create target directories (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_libdir}/ladspa/ \
			%{buildroot}%{_includedir}/ladspa/ \
			%{buildroot}%{_bindir}/ladspa/
%makeinstall -C src

%post
/sbin/ldconfig &>/dev/null

%postun
/sbin/ldconfig &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README doc/COPYING
%{_libdir}/ladspa/
%{_bindir}/*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*.html
%{_includedir}/*.h

%changelog
* Fri Mar  5 2004 Matthias Saou <http://freshrpms.net/> 1.12-0
- Branch off temporarily to build gstramer07-plugins.

* Thu Feb 19 2004 Dag Wieers <dag@wieers.com> - 1.12-1
- Obsoletes ladspa-sdk. (Rudolf Kastl, #15)

* Sun Sep 14 2003 Dag Wieers <dag@wieers.com> - 1.12-0
- Initial package. (using DAR)

