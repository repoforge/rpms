# $Id: _template.spec 201 2004-04-03 15:24:49Z dag $
# Authority: dag
# Upstream: <gnupg-devel$gnupg,org>

Summary: PIN or passphrase entry dialog
Name: pinentry
Version: 0.6.8
Release: 1
License: GPL
Group: Applications/System
URL: http://www.gnupg.org/aegypten/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.gnupg.org/gcrypt/alpha/aegypten/pinentry-%{version}.tar.gz
Patch: %{name}-info.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib-devel >= 1:1.2.0, gtk+-devel >= 1:1.2.0, qt-devel
BuildRequires: ncurses-devel
Requires: chkconfig, info

%description
This is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.

%prep
%setup
%patch0 -p0

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

touch %{buildroot}%{_bindir}/pinentry

### Clean up buildroot
%{__rm} -f %{buildroot}%{_infodir}/dir

%post
install-info %{_infodir}/pinentry.info.gz %{_infodir}/dir
update-alternatives --install %{_bindir}/pinentry pinentry %{_bindir}/pinentry-curses 10
update-alternatives --install %{_bindir}/pinentry pinentry %{_bindir}/pinentry-gtk 40
update-alternatives --install %{_bindir}/pinentry pinentry %{_bindir}/pinentry-qt 30

%postun
if [ $1 -eq 0 ]; then
	install-info --delete %{_infodir}/pinentry.info.gz %{_infodir}/dir
	update-alternatives --remove pinentry %{_bindir}/pinentry-curses
	update-alternatives --remove pinentry %{_bindir}/pinentry-gtk
	update-alternatives --remove pinentry %{_bindir}/pinentry-qt
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%doc %{_infodir}/*.info*
%{_bindir}/pinentry-*
%ghost %{_bindir}/pinentry

%changelog
* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 0.6.8-1
- Initial package. (using DAR)
