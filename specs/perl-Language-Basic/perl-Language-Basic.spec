# $Id$
# Authority: dries
# Upstream: Amir Karger <amirkargerweb$yahoo,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Language-Basic

Summary: Interpret BASIC
Name: perl-Language-Basic
Version: 1.44
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Language-Basic/

Source: http://search.cpan.org/CPAN/authors/id/A/AK/AKARGER/Language-Basic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Language::Basic is a Perl module implementation of the BASIC computer language
It allows you to run BASIC programs or translate them to Perl scripts.
Note that it implements 80's-era BASIC. Think Applesoft or GW-BASIC.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{_bindir}/basic.pl
%{_bindir}/basic2pl.pl
%{_bindir}/termbasic.pl
%{perl_vendorlib}/Language/Basic.pm
%{perl_vendorlib}/Language/Basic

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.44-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.44-1
- Initial package.
