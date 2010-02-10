# $Id$
# Authority: shuff
# Upstream: Jeffrey Hayes Anderson <captvanhalen$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-XHTML_Table

Summary: SQL query result set to XML-based HTML table
Name: perl-%{real_name}
Version: 1.36
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-XHTML_Table/

Source: http://search.cpan.org/CPAN/authors/id/J/JE/JEFFA/DBIx-XHTML_Table-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(DBI) >= 1.20
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(DBI) >= 1.20


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
DBIx::XHTML_Table is a DBI extension that creates an XHTML table from a
database query result set. It was created to fill the gap between fetching rows
from a database and transforming them into a web browser renderable table.
DBIx::XHTML_Table is intended for programmers who want the responsibility of
presenting (decorating) data, easily. This module is meant to be used in
situations where the concern for presentation and logic seperation is overkill.
Providing logic or editable data is beyond the scope of this module, but it is
capable of doing such.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/DBIx/
%{perl_vendorlib}/DBIx/*

%changelog
* Thu Feb 04 2010 Steve Huff <shuff@vecna.org> - 1.36-1
- Initial package.
