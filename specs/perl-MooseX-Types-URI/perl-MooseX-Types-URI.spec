# $Id$
# Authority: shuff
# Upstream: Florian Ragwitz <rafl$debian,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-Types-URI

Summary: URI-related types and coercions for Moose
Name: perl-MooseX-Types-URI
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-Types-URI/

Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/MooseX-Types-URI-0.02.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose) >= 0.50
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(MooseX::Types::Path::Class)
BuildRequires: perl(namespace::clean) >= 0.08
BuildRequires: perl(Test::use::ok)
BuildRequires: perl(URI)
BuildRequires: perl(URI::FromHash)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Moose) >= 0.50
Requires: perl(MooseX::Types)
Requires: perl(MooseX::Types::Path::Class)
Requires: perl(namespace::clean) >= 0.08
Requires: perl(URI)
Requires: perl(URI::FromHash)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# damn it Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

# fix for stupid strip issue
%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml SIGNATURE
%doc %{_mandir}/man?/*
%{perl_vendorlib}/MooseX/Types/URI.pm
#%{perl_vendorlib}/MooseX/Types/URI/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Thu Feb 24 2011 Steve Huff <shuff@vecna.org> - 0.02-1
- Initial package.
