# $Id$
# Authority: dries
# Upstream: Mirko Westermeier <mail$memowe,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-SBC

Summary: Simple blog code for valid XHTML and HTML
Name: perl-HTML-SBC
Version: 0.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-SBC/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-SBC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::Exception)
#BuildRequires: perl(Test::Simple) >= 0.62
#BuildRequires: perl(Test::More) >= 0.62
BuildRequires: perl(Carp)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Exporter) >= 5.58

%description
Simple blog code (SBC) is a simple markup language, You can use it for guest
books, blogs, wikis, boards and various other web applications. It produces
valid and semantic (X)HTML from input and is patterned on that tiny usenet
markups like *bold* and _underline_.

HTML::SBC tries to give useful error messages and guess the right translation
even with invalid input. It will always produce valid (X)HTML.

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
%dir %{perl_vendorlib}/HTML/
%{perl_vendorlib}/HTML/SBC.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Updated to release 0.15.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Initial package.
