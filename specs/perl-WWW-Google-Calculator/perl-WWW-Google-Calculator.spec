# $Id$
# Authority: shuff
# Upstream: Daisuke Murase <typester$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Google-Calculator

Summary: Perl interface for Google Calculator
Name: perl-WWW-Google-Calculator
Version: 0.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Google-Calculator/

Source: http://search.cpan.org/CPAN/authors/id/T/TY/TYPESTER/WWW-Google-Calculator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Filter::Util::Call)
BuildRequires: perl(HTML::TokeParser)
BuildRequires: perl(WWW::Mechanize)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Class::Accessor::Fast)
Requires: perl(Filter::Util::Call)
Requires: perl(HTML::TokeParser)
Requires: perl(WWW::Mechanize)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module provides a simple interface for Google Calculator.

http://www.google.com/help/calculator.html

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE META.yml README Todo
%doc %{_mandir}/man?/*
%{perl_vendorlib}/WWW/Google/Calculator.pm
#%{perl_vendorlib}/WWW/Google/Calculator/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Fri Jun 03 2011 Steve Huff <shuff@vecna.org> - 0.07-1
- Initial package.
