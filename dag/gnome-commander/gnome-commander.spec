# Authority: newrpms
# Upstream: Marcus Bjurman <marbj499 at student.liu.se>, <gcmd-devel@nongnu.org>

Summary: A file manager similar to the Norton Commander (TM).
Name: gnome-commander
Version: 1.0.1
Release: 0
License: GPL
Group: Applications/File
URL: http://www.nongnu.org/gcmd/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://savannah.nongnu.org/download/gcmd/gcmd.pkg/%{version}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gnome-vfs-devel >= 0.5, glib2-devel, intltool
Requires: gettext >= 0.10.36

%description
Gnome Commander is a file manager that just like the classical Norton Commander (TM) lets you do everything with the keyboard. It can perform all standard file operations and some extra features like FTP support.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO doc/
%{_bindir}/*
%{_datadir}/gnome/apps/Applications/gnome-commander.desktop
%{_datadir}/pixmaps/gnome-commander/

%changelog
* Sat Nov 08 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Initial package. (using DAR)
