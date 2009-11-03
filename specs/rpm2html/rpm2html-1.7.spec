# $Id$
# Authority: dag

# ExclusiveDist: rh7

%{?dtag: %{expand %%define: %dist 1}}

Summary: Translates an RPM database and dependency information into HTML
Name: rpm2html
Version: 1.7
Release: 0%{?dist}
Group: Applications/System
License: MIT
URL: http://rpmfind.net/linux/rpm2html/

Source: ftp://rpmfind.net/pub/rpm2html/rpm2html-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: rpm-devel, db3-devel

%description
The rpm2html utility automatically generates web pages that describe a
set of RPM packages.  The goals of rpm2html are to identify the
dependencies between various packages, and to find the package(s) that
will provide the resources needed to install a given package.
Rpm2html analyzes the provides and requires of the given set of RPMs,
and then shows the dependency cross-references using hypertext links.
Rpm2html can now dump the metadata associated with RPM files into
standard RDF files.

Install rpm2html if you want a utility for translating information
from an RPM database into HTML.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags} \
%{?rh7:	LIBXML_FLAGS="-I/usr/include/libxml2 -I/usr/include/libxml2/libxml"}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 rpm2html %{buildroot}%{_bindir}/rpm2html
%{__install} -Dp -m0644 rpm2html.config  %{buildroot}%{_sysconfdir}/rpm2html.config
%{__install} -Dp -m0644 rpm2html.1  %{buildroot}%{_mandir}/man1/rpm2html.1

for i in msg.*; do
  %{__install} -Dp -m0644 $i %{buildroot}%{_datadir}/rpm2html/msg.$ll
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGES PRINCIPLES README TODO
%doc rpm2html-cdrom.config rpm2html-en.config
%doc %{_mandir}/man1/rpm2html.1*
%config %{_sysconfdir}/rpm2html.config
%{_bindir}/rpm2html
%{_datadir}/rpm2html/

%changelog
* Mon Feb 10 2003 Dag Wieers <dag@wieers.com> - 1.7
- Initial package. (using DAR}
