# $Id$
# Authority: dag
# Upstream: Szabolcs Szakacsits <szaka$ntfs-3g,org>

Summary: Find NTFS partitions
Name: findntfs
Version: 1.3
Release: 1
License: GPL
Group: Applications/System
URL: http://mlf.linux.rulez.org/mlf/ezaz/ntfsresize.html#troubleshoot

Source: http://mlf.linux.rulez.org/mlf/ezaz/findntfs-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
findntfs is a tool to find NTFS filesystems.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS FAQ INSTALL LICENSE NEWS README THANKS TODO
%{_bindir}/findntfs

%changelog
* Sat Nov 08 2008 Dag Wieers <dag@wieers.com> - 1.3-1
- Initial package. (using DAR)
