# $Id$
# Authority: shuff
# Upstream: Adam Kaplan <akaplan$cpan,org>, Tim Bunce <timb$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-NYTProf

Summary: Powerful fast feature-rich perl source code profiler
Name: perl-%{real_name}
Version: 4.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-NYTProf/

Source: http://search.cpan.org/CPAN/authors/id/T/TI/TIMB/Devel-NYTProf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 5.8.1
BuildRequires: perl(Config)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(JSON::Any)
BuildRequires: perl(List::Util)
# BuildRequires: perl(Test::More) >= 0.84
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.1
Requires: perl(Getopt::Long)
Requires: perl(JSON::Any)
Requires: perl(List::Util)
Requires: perl(XSLoader)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Powerful fast feature-rich perl source code profiler

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

# move the command-line stuff into place
%{__install} -m0755 -d %{buildroot}%{_bindir}
%{__mv} %{buildroot}%{perl_vendorarch}/Devel/*.pl %{buildroot}%{_bindir}

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README demo/
%doc %{_mandir}/man?/*
%dir %{perl_vendorarch}/Devel/NYTProf/
%{perl_vendorarch}/Devel/NYTProf.pm
%{perl_vendorarch}/Devel/NYTProf/*
%{perl_vendorarch}/Devel/auto/Devel/*
%{perl_vendorarch}/auto/Devel/*
%{_bindir}/*

%changelog
* Thu Jul 29 2010 Steve Huff <shuff@vecna.org> - 4.04-1
- Updated to release 4.04.

* Tue May 25 2010 Steve Huff <shuff@vecna.org> - 3.11-1
- Initial package (thanks to Philip Durbin).
