# $Id$
# Authority: dag
# Upstream: Christian Glodt <chris$mind,lu>

Summary: Mozilla plugin for using bonobo components
Name: mozilla-bonobo
Version: 0.4.1
Release: 2.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.nongnu.org/moz-bonobo/

Source: http://savannah.nongnu.org/download/moz-bonobo/mozilla-bonobo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mozilla-devel >= 1.0, mozilla-nspr-devel >= 1.0
BuildRequires: gtk2-devel >= 2.0, glib2-devel >= 2.0, pango-devel >= 1.0.0
BuildRequires: atk-devel >= 1.0, freetype-devel >= 2.0
BuildRequires: gcc-c++, libgnomeprint22-devel
BuildRequires: libgnomeui-devel
#BuildRequires: libbonoboui
#Requires: %{_libdir}/mozilla/plugins/

%description
This package contains a plugin for the Mozilla browser that makes it
possible to use bonobo components.

%prep
%setup

%build
%configure \
	--with-plugin-install-dir="%{buildroot}%{_libdir}/mozilla/plugins" \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}/mozilla/plugins/
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q

%postun
scrollkeeper-update -q

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_libdir}/mozilla/plugins/*.so
%exclude %{_prefix}/doc/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.1-2.2
- Rebuild for Fedora Core 5.

* Fri Nov 19 2004 Dag Wieers <dag@wieers.com> - 0.4.1-2
- Removed %%{_libdir}/mozilla/plugins/

* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Updated to release 0.4.1.

* Fri Oct 03 2003 Dag Wieers <dag@wieers.com> - 0.4.0-0
- Updated to release 0.4.0.

* Wed Jul 23 2003 Dag Wieers <dag@wieers.com> - 0.3.0-1
- Build against mozilla release 1.4.

* Tue May 20 2003 Dag Wieers <dag@wieers.com> - 0.3.0-0
- Updated to release 0.3.0.

* Fri May 09 2003 Dag Wieers <dag@wieers.com> - 0.2.0-0
- Updated to release 0.2.0.

* Thu May 08 2003 Dag Wieers <dag@wieers.com> - 0.1.0-0
- Initial package. (using DAR)
