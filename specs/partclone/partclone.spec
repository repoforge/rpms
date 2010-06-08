# $Id$
# Authority: dag

Summary: File system clone utility for ext2/3/4, reiserfs, reiser4, xfs, hfs+
Name: partclone
Version: 0.2.8
Release: 1
License: GPL
Group: Applications/System
URL: http://partclone.org/

#Source: http://dl.sf.net/project/partclone/stable/0.2.8/partclone-%{version}.tar.gz
Source: http://partclone.nchc.org.tw/download/stable/%{version}/partclone_%{version}.tar.gz
#BuildRequires: e2fsprogs-devel >= 1.41.3
BuildRequires: e2fsprogs-devel
BuildRequires: e2fsprogs-devel
BuildRequires: ncurses-devel
BuildRequires: ntfsprogs-devel
#BuildRequires: progsreiserfs
#BuildRequires: reiser4progs
#BuildRequires: xfsprogs-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A set of file system clone utilities, including
ext2/3, reiserfs, reiser4, xfs, hfs+ file system

%prep
%setup

%{__perl} -pi -e 's|41|31|g' configure

%build
%configure \
    --disable-ext4 \
    --enable-all \
    --enable-ncursesw \
    --enable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man8/clone.extfs.8*
%doc %{_mandir}/man8/clone.fat.8*
%doc %{_mandir}/man8/clone.hfsp.8*
%doc %{_mandir}/man8/clone.reiser4.8*
%doc %{_mandir}/man8/clone.reiserfs.8*
%doc %{_mandir}/man8/clone.xfs.8*
%{_sbindir}/clone.ext2
%{_sbindir}/clone.ext3
#%{_sbindir}/clone.ext4
%{_sbindir}/clone.extfs
%{_sbindir}/clone.fat
%{_sbindir}/clone.hfsp
%{_sbindir}/clone.reiser4
%{_sbindir}/clone.reiserfs
%{_sbindir}/clone.xfs
%{_sbindir}/clone.info

%changelog
* Thu May 27 2010 Dag Wieers <dag@wieers.com> - 0.2.8-1
- Initial package. (using DAR)
