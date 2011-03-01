# $Id$
# Authority: shuff
# Upstream: David Golden <dagolden$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Amazon-Config

Summary: Manage Amazon Web Services credentials
Name: perl-Net-Amazon-Config
Version: 0.001
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Amazon-Config/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/Net-Amazon-Config-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(Config::Tiny) >= 2.12
BuildRequires: perl(File::Find)
# BuildRequires: perl(File::Spec) >= 3.31
BuildRequires: perl(File::Spec)
BuildRequires: perl(Object::Tiny) >= 1.06
BuildRequires: perl(Params::Validate) >= 0.91
BuildRequires: perl(Path::Class) >= 0.17
# BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
BuildRequires: perl(constant) >= 1
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp)
Requires: perl(Config::Tiny) >= 2.12
Requires: perl(Object::Tiny) >= 1.06
Requires: perl(Params::Validate) >= 0.91
Requires: perl(Path::Class) >= 0.17
Requires: perl(constant) >= 1

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module lets you keep Amazon Web Services credentials in a configuration
file for use with different tools that need them.

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
%doc Changes INSTALL LICENSE META.yml README Todo
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Net/Amazon/Config.pod
%{perl_vendorlib}/Net/Amazon/Config.pm
%{perl_vendorlib}/Net/Amazon/Config/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Tue Mar 01 2011 Steve Huff <shuff@vecna.org> - 0.001-1
- Initial package.
