# $Id$
# Authority: dries
# Upstream: Paul Sharpe <paul$miraclefish,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name TextStructured

Summary: Manipulate fixed-format pages
Name: perl-TextStructured
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/TextStructured/

Source: http://search.cpan.org/CPAN/authors/id/P/PS/PSHARPE/TextStructured-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Text::Structured is a class for manipulating fixed-format pages of
text.  It contains methods for extracting text from the page.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" "PREFIX=%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/Structured.pm
%{perl_vendorlib}/Text/StructuredBase.pm

%changelog
* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
