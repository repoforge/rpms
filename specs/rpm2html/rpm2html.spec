# $Id$
# Authority: dag

Summary: Translates an RPM database and dependency information into HTML
Name: rpm2html
Version: 1.8.2
Release: 0.2%{?dist}
License: MIT
Group: Applications/System
URL: http://rpmfind.net/linux/rpm2html/

Source: ftp://rpmfind.net/pub/rpm2html/rpm2html-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: rpm-devel, zlib-devel, bzip2-devel, popt, libxml2-devel
BuildRequires: automake, autoconf, db4-devel, automake16
Requires: gnupg

%description
The rpm2html utility automatically generates web pages that describe a
set of RPM packages.  The goals of rpm2html are to identify the
dependencies between various packages, and to find the package(s) that
will provide the resources needed to install a given package.
Rpm2html analyzes the provides and requires of the given set of RPMs,
and then shows the dependency cross-references using hypertext links.
Rpm2html can now dump the metadata associated with RPM files into
standard RDF files.

%prep
%setup

%build
%configure \
	--with-gpg
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGES Copyright PRINCIPLES README TODO
%doc rpm2html-cdrom.config rpm2html-en.config rpm2html-rdf.config
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/rpm2html.config
%{_bindir}/*
%{_datadir}/rpm2html/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.8.2-0.2
- Rebuild for Fedora Core 5.

* Thu Feb 26 2004 Dag Wieers <dag@wieers.com> - 1.8.2-0
- Updated to release 1.8.2.

* Mon Feb 10 2003 Dag Wieers <dag@wieers.com> - 1.7-0
- Initial package. (using DAR)
