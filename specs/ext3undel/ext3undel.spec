# $Id$
# Authority: dag
# Upstream: 

Summary: Tools to help you recover files from ext2/ext3 filesystems
Name: ext3undel
Version: 0.1.6
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://projects.izzysoft.de/trac/ext3undel

Source: ext3undel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch

%description
Though most pages in the InterNet state it is impossible to undelete such files,
this is simply wrong. Correct is: It is not that easy as to simply take them out
of some trash folder. Using forensic tools, as e.g. Sleuthkit, PhotoRec and
foremost, the task is possible - but may require a lot of manual work. ext3undel
tries to automate most of this - so it is possible to recover a single specified
file - or all data on a given disk.

%prep
%setup

%build
#configure
#%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/*
%doc %{_mandir}/man5/ext3undel.conf.5*
%doc %{_mandir}/man8/ext3undel.8*
%doc %{_mandir}/man8/gabi.8*
%doc %{_mandir}/man8/ralf.8*
%config %{_sysconfdir}/ext3undel/
%{_bindir}/ext3undel
%{_bindir}/gabi
%{_bindir}/ralf
%exclude %{_docdir}/ext3undel/

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 0.1.6-1
- Initial package. (using DAR)
