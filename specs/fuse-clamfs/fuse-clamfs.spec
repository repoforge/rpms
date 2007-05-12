# $Id$
# Authority: dag

%define real_name clamfs

Summary: FUSE-based user-space file system for Linux with on-access anti-virus file scanning
Name: fuse-clamfs
Version: 0.9.1
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://clamfs.sourceforge.net/

Source: http://dl.sf.net/clamfs/clamfs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fuse-devel >= 2.2, rlog-devel, poco-devel
Requires: fuse >= 2.2

Obsoletes: clamfs <= %{name}-%{version}
Provides: clamfs = %{name}-%{version}

%description
FUSE-based user-space file system for Linux with on-access anti-virus
file scanning through clamd daemon.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
	--disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{real_name}

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
#%doc AUTHORS BUGS COPYING FAQ INSTALL NEWS README* THANKS TODO etc/davfs2.conf etc/secrets
#%doc %{_mandir}/man5/davfs2.conf.5*
#%doc %{_mandir}/man8/mount.davfs.8*
#%doc %{_mandir}/man8/umount.davfs.8*
#%doc %{_mandir}/*/man5/davfs2.conf.5*
#%doc %{_mandir}/*/man8/mount.davfs.8*
#%doc %{_mandir}/*/man8/umount.davfs.8*
#%config(noreplace) %{_sysconfdir}/davfs2/davfs2.conf
#%config %{_sysconfdir}/davfs2/secrets
#%config %{_sysconfdir}/davfs2/certs/
#/sbin/mount.davfs
#/sbin/umount.davfs
#%{_datadir}/davfs2/

%changelog
* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Initial package. (using DAR)
