# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Graphical tool acquiring and tracking Kerberos V tickets
Name: gktools
Version: 0.10.2
Release: 1%{?dist}
License: GPL
Group: User Interface/X
URL: http://asgaard.homelinux.org/code/gktools/

Source: http://asgaard.homelinux.org/code/gktools/gktools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: automake >= 1.9, gtk2-devel, libglade2-devel, krb5-devel, perl-XML-Parser
BuildRequires: desktop-file-utils
Conflicts: gnome-kerberos

%description
gktools contains two graphical tools for the MIT Kerberos V distribution.
gkinit is a graphical tool for acquiring tickets (like kinit) and gktickets
is a graphical tool for listing and tracking kerberos tickets.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__mv} -f %{buildroot}%{_datadir}/applications/fedora-gktickets.desktop gtickets.desktop
%{__mkdir_p} %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}     \
	--delete-original                           \
	--add-category=Application                  \
	--add-category=Utility                      \
               --dir %{buildroot}%{_datadir}/applications  \
	gtickets.desktop

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/gkinit
%{_bindir}/gktickets
%{_datadir}/gktools/
%{_datadir}/pixmaps/gktools.png
%{_datadir}/applications/%{desktop_vendor}-gtickets.desktop

%changelog
* Fri Feb 16 2007 Dag Wieers <dag@wieers.com> - 0.10.2-1
- Initial package. (using DAR)
