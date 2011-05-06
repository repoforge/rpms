# $Id$
# Authority: shuff
# Upstream: Karl Gaissmaier <karl.gaissmaier$uni-ulm,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-Scoped

Summary: feature-rich configuration file parser
Name: perl-Config-Scoped
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Scoped/

Source: http://search.cpan.org/CPAN/authors/id/G/GA/GAISSMAI/Config-Scoped-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Error)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Parse::RecDescent) >= 1.94
BuildRequires: perl(Safe)
BuildRequires: perl(Storable)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp)
Requires: perl(Digest::MD5)
Requires: perl(Error)
Requires: perl(File::Basename)
Requires: perl(File::Spec)
Requires: perl(Parse::RecDescent) >= 1.94
Requires: perl(Safe)
Requires: perl(Storable)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Config::Scoped is a configuration file parser.

Features:
* recursive data structures with scalars, lists, and hashes
* parses ISC named and dhcpd config files
* parses many Perl data structures without eval, do or require
* Perl quoting syntax: single quotes (''), double quotes(""), and here docs
  (<<EOF)
* Perl code evaluation in Safe compartments
* simplified syntax with minimal punctuation
* include files with recursion checks
* controlled macro expansion in double quoted tokens
* lexically scoped parameter assignments and directives
* duplicate macro, parameter, and declaration checks
* file permission and ownership safety checks
* fine control over error checking
* error messages report config file names and line numbers
* exception-based error handling
* Parse::RecDescent-based parser; precompiled grammar for speed
* configuration caching with MD5 checksums on the original files
* may be subclassed to build parsers with specialized features


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
%doc Changes META.yml README example/
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Config/Scoped.pm
%{perl_vendorlib}/Config/Scoped.pod
%{perl_vendorlib}/Config/Scoped/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri May 06 2011 Steve Huff <shuff@vecna.org> - 0.13-1
- Initial package.
