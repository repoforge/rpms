# $Id$
# Authority: shuff
# Upstream: I. Yu. Vlasenko <viy$altlinux,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Template-Pro

Summary: Perl/XS module to use HTML Templates from CGI scripts
Name: perl-HTML-Template-Pro
Version: 0.9502
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Template-Pro/

Source: http://search.cpan.org/CPAN/authors/id/V/VI/VIY/HTML-Template-Pro-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# BuildArch: noarch
BuildRequires: pcre-devel
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
# BuildRequires: perl(File::Path) >= 2
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(JSON) >= 2
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
# Requires: perl(File::Path) >= 2
Requires: perl(File::Path)
Requires: perl(File::Spec)
Requires: perl(JSON) >= 2

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
HTML::Template::Pro is a fast lightweight C/Perl+XS reimplementation of
HTML::Template (as of 2.9) and HTML::Template::Expr (as of 0.0.7). It is not
intended to be a complete replacement, but to be a fast implementation of
HTML::Template if you don't need quering, the extended facility of
HTML::Template. Designed for heavy upload, resource limitations, abcence of
mod_perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ARTISTIC Changes META.yml README TODO
%doc %{_mandir}/man?/*
%{perl_vendorarch}/HTML/Template/Pro.pm
%{perl_vendorarch}/HTML/Template/*.pod
%{perl_vendorarch}/HTML/Template/Pro/*
%{perl_vendorarch}/auto/HTML/Template/Pro/*
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Thu Aug 26 2010 Steve Huff <shuff@vecna.org> - 0.9502-1
- Initial package.
