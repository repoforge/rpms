# $Id$
# Authority: dag
# Upstream: Ali Akcaagac <aliakc$web,de>

# Tag: rft

Summary: Light-weight GNOME web browser
Name: atlantis
Version: 0.1.3
Release: 1.2%{?dist}
License: Proprietary/Binary Only
Group: Applications/Internet
URL: http://www.akcaagac.com/index_atlantis.html

Source: http://www.akcaagac.com/atlantis/files/atlantis-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386
BuildRequires: gtkhtml2 >= 2.0

%description
Light-weight GNOME web browser.

%prep
%setup -c

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}
tar -xvjf %{_builddir}/%{buildsubdir}/%{name}.tar.bz2 -C %{buildroot}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%config %{_sysconfdir}/gconf/schemas/atlantis.schemas
%{_bindir}/atlantis
%{_datadir}/atlantis/
%{_datadir}/applications/atlantis.desktop
%{_datadir}/application-registry/atlantis.applications
%{_datadir}/pixmaps/atlantis.png

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.3-1.2
- Rebuild for Fedora Core 5.

* Mon May 02 2005 Dag Wieers <dag@wieers.com> - 0.1.3-1
- Updated to release 0.1.3.

* Mon Jun 23 2003 Dag Wieers <dag@wieers.com> - 0.1.2-0
- Updated to release 0.1.2.

* Thu Jun 12 2003 Dag Wieers <dag@wieers.com> - 0.1.1-0
- Updated to release 0.1.1.

* Sun May 11 2003 Dag Wieers <dag@wieers.com> - 0.1.0-0
- Initial package. (using DAR)
