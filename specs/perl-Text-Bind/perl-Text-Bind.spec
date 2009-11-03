# $Id$
# Authority: dries
# Upstream: Earl Hood <ehood$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Bind

Summary: Bind Perl structures to text files
Name: perl-Text-Bind
Version: 0.04
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Bind/

Source: http://www.cpan.org/modules/by-module/Text/Text-Bind-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Text::Bind allows you to bind Perl structures (strings, routines,
filehandles, objects, and arrays) to specific locations (called *data
sites*) in text files.

The main purpose of this module is to support HTML templates for
CGI programs. Therefore, HTML pages design can be kept separate from
CGI code. However, the class is general enough to be used in other
contexts than CGI application development.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/Bind.pm

%changelog
* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
