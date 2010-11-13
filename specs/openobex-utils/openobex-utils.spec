# $Id$
# Authority: dag

%define real_name openobex-apps

Summary: Utilities based on Openobex
Name: openobex-utils
Version: 1.0.0
Release: 1.2%{?dist}
License: LGPL
Group: System Environment/Base
URL: http://openobex.sourceforge.net/

Source0: http://dl.sf.net/openobex/openobex-apps-%{version}.tar.gz
Source1: http://www.frasunek.com/sources/unix/obexserver.c
Patch0: openobex-apps-1.0.0-gcc3.4.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openobex-devel
Obsoletes: openobex-apps <= %{release}
Provides: openobex-apps

%description
Utilities based on Openobex.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Ugly (smart?) hack to have obexserver when bluetooth is compiled in openobex.
cd src
${CC:-%{__cc}} %{optflags} -o obexserver %{SOURCE1} libmisc.a $(openobex-config --libs) && \
%{__install} -Dp -m0755 obexserver %{buildroot}%{_bindir}/obexserver || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/irobex_palm3
%{_bindir}/irxfer
%{_bindir}/obexserver
%{_bindir}/obex_tcp
%{_bindir}/obex_test

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.0-1.2
- Rebuild for Fedora Core 5.

* Mon Jan 30 2006 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Added patch for gcc 3.4+.

* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Initial package. (using DAR)
