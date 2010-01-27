# $Id$
# Authority: shuff
# Upstream: <pmarek$tigris,org>

Summary: Backup/restore/versioning of large data sets with meta-data
Name: fsvs
Version: 1.2.1
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://freshmeat.net/projects/fsvs

Source: http://download.fsvs-software.org/fsvs-%{version}.tar.gz
Patch0: fsvs-1.2.1_destdir.patch
Patch1: fsvs-1.2.1_manpages.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: apr-devel
BuildRequires: ctags
BuildRequires: gdbm-devel
BuildRequires: pcre-devel
BuildRequires: subversion-devel
Requires: ctags

Provides: %{_bindir}/fsvs

%description
FSVS is the abbreviation for “Fast System VerSioning”, and is pronounced
[fisvis].

It is a complete backup/restore/versioning tool for all files in a directory
tree or whole filesystems, with a subversionTM repository as the backend.  You
may think of it as some kind of tar or rsync with versioned storage. 

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE README doc/ example/
%doc %{_mandir}/man?/*
%{_bindir}/*
%attr(0755, root, root) %dir %{_localstatedir}/spool/fsvs
%attr(0777, root, root) %dir %{_sysconfdir}/fsvs
%config(noreplace) %{_sysconfdir}/fsvs/*

%changelog
* Mon Jan 25 2010 Steve Huff <shuff@vecna.org> - 1.2.1-1
- Initial commit.
