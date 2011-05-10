# $Id$
# Authority: shuff
# Upstream: Graham TerMarsch <cpan$howlingfrog,com>
# ExcludeDist: el3 el4

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CSS-Minifier-XS

Summary: XS-based CSS minifier
Name: perl-CSS-Minifier-XS
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CSS-Minifier-XS/

Source: http://search.cpan.org/CPAN/authors/id/G/GT/GTERMARS/CSS-Minifier-XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# BuildArch: noarch
BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: perl >= 5.8.8
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.8

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
CSS::Minifier::XS is a CSS "minifier"; its designed to remove un-necessary
whitespace and comments from CSS files, while also not breaking the CSS.
CSS::Minifier::XS is similar in function to CSS::Minifier, but is substantially
faster as its written in XS and not just pure Perl.

CSS::Minifier::XS minifies the CSS by removing un-necessary whitespace from CSS
documents. Comment blocks are also removed, except when (a) they contain the
word "copyright" in them, or (b) they're needed to implement the "Mac/IE
Comment Hack".

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/CSS/Minifier/XS.pm
%{perl_vendorarch}/auto/CSS/Minifier/XS/*
#%{perl_vendorlib}/CSS/Minifier/XS/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Tue May 10 2011 Steve Huff <shuff@vecna.org> - 0.08-1
- Initial package.
