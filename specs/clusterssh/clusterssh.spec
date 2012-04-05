# $Id$
# Authority: duncan
# Upstream: Duncan Ferguson <duncan_ferguson$users,sf,net>

%define perl_version %(eval "$(%{__perl} -V:version)"; echo $version)

%define desktop_vendor rpmforge

Summary: Secure concurrent multi-server terminal control
Name: clusterssh
Version: 3.28
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://clusterssh.sourceforge.net/

Source: http://download.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl => 1:5.6.1, perl(Tk), perl(X11::Protocol), desktop-file-utils
Requires: perl(:MODULE_COMPAT_%{perl_version})

%description
Control multiple terminals open on different servers to perform administration
tasks, for example multiple hosts requiring the same config within a cluster.
Not limited to use with clusters, however.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 clusterssh-24x24.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/clusterssh.png
%{__install} -Dp -m0644 clusterssh-32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/clusterssh.png
%{__install} -Dp -m0644 clusterssh-48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/clusterssh.png
%{__mkdir_p} %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	clusterssh.desktop

%post
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%postun
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/cssh.1*
%{_bindir}/cssh
%{_datadir}/applications/%{desktop_vendor}-clusterssh.desktop
%{_datadir}/icons/hicolor/24x24/apps/clusterssh.png
%{_datadir}/icons/hicolor/32x32/apps/clusterssh.png
%{_datadir}/icons/hicolor/48x48/apps/clusterssh.png

%changelog
* Mon Feb 20 2012 David Hrbáč <david@hrbac.cz> - 3.28-1
- new upstream release

* Wed Jan 24 2007 Dag Wieers <dag@wieers.com> - 3.19.1-1
- Updated to release 3.19.1.

* Thu Aug 18 2005 Duncan Ferguson <duncan_ferguson@users.sf.net> - 3.17.1-1
- Initial version.
