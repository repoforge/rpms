# $Id$
# Authority: shuff
# Upstream: Thomas A. Lowery <talowery$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBI-Shell

Summary: Interactive command shell for the DBI
Name: perl-%{real_name}
Version: 11.95
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBI-Shell/

Source: http://search.cpan.org/CPAN/authors/id/T/TL/TLOWERY/DBI-Shell-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(DBI)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::Tee)
BuildRequires: perl(Text::CSV)
BuildRequires: perl(Text::Reform)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(DBI)
Requires: perl(IO::Tee)
Requires: perl(Text::CSV)
Requires: perl(Text::Reform)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
The DBI::Shell module (and dbish command, if installed) provide a simple but
effective command line interface for the Perl DBI module.

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
%dir %{perl_vendorlib}/DBI/
%{perl_vendorlib}/DBI/*
%{_bindir}/*

%changelog
* Tue Feb 09 2010 Steve Huff <shuff@vecna.org> - 11.95-1
- Initial package.
