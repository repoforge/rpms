# $Id$

# Authority: dag

Summary: Graphical .lircrc configuration program
Name: lircrc_config
Version: 0.1.1
Release: 0.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.lirc.org/

Source: http://dl.sf.net/lirc/lircrc_config-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk+-devel, glib2-devel, lirc, glib-devel
BuildRequires: libglade-devel, lirc-devel, flex

%description
A GNOME .lircrc configuration program.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README samples/ TODO
%{_bindir}/*
%{_datadir}/lircrc_config/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.1-0.2
- Rebuild for Fedora Core 5.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.1.1-0
- Initial package. (using DAR)
