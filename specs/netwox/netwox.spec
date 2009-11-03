# $Id$
# Authority: dries
# Upstream: Laurent Constantin <laurent,constantin$aql,fr>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Toolbox for solving network problems
Name: netwox
Version: 5.35.0
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.laurentconstantin.com/en/netw/netwox/

Source: http://www.laurentconstantin.com/common/netw/netwox/download/v5/netwox-%{version}-src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: netwib, pkgconfig, libpcap, libnet
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
Netwox is a toolbox that helps to find and solve networks' problems.

%prep
%setup -n %{name}-%{version}-src
%{__perl} -pi -e 's|^NETWIBDEF_INSTPREFIX=.*|NETWIBDEF_INSTPREFIX=%{_prefix}|g;' src/config.dat

%build
cd src
./genemake
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd src
%makeinstall INSTINCLUDE=%{buildroot}%{_includedir} INSTLIB=%{buildroot}%{_libdir} INSTBIN=%{buildroot}%{_bindir} INSTMAN3=%{buildroot}%{_mandir}/man3 INSTMAN1=%{buildroot}%{_mandir}/man1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.TXT
%doc %{_mandir}/man1/netwox*
%{_bindir}/netwox*

%changelog
* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 5.35.0-1
- Updated to release 5.35.0.

* Fri Apr 07 2006 Dries Verachtert <dries@ulyssis.org> - 5.34.0-1
- Updated to release 5.34.0.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 5.33.0-1
- Updated to release 5.33.0.

* Sun Nov 27 2005 Dries Verachtert <dries@ulyssis.org> - 5.32-1
- Initial package.
