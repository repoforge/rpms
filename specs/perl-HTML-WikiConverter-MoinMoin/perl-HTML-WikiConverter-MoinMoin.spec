# $Id$
# Authority: shuff
# Upstream: David Iberri <diberri$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-WikiConverter-MoinMoin

Summary: Converts HTML to MoinMoin markup
Name: perl-HTML-WikiConverter-MoinMoin
Version: 0.54
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-WikiConverter-MoinMoin/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-WikiConverter-MoinMoin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::WikiConverter) >= 0.63
BuildRequires: perl(Params::Validate)
BuildRequires: perl(URI)
Requires: perl(HTML::WikiConverter) >= 0.63

%description
HTML::WikiConverter::MoinMoin adds the MoinMoin dialect to
HTML::WikiConverter allowing the conversion of HTML to MoinMoin
markup.

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
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/HTML/WikiConverter/
%{perl_vendorlib}/HTML/WikiConverter/*

%changelog
* Fri Feb 05 2010 Steve Huff <shuff@vecna.org> - 0.54-1
- Initial package.
