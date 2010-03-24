# $Id$
# Authority: shuff
# Upstream: Matt Cashner <sungo$sungo,us>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Dropbox

Summary: Communicate with local Dropbox daemon
Name: perl-%{real_name}
Version: 1.091510
Release: 1%{?dist}
License: BSD
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Dropbox/

Source: http://search.cpan.org/CPAN/authors/id/S/SU/SUNGO/Net-Dropbox-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::HomeDir)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::StrictConstructor)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Encode)
Requires: perl(File::HomeDir)
Requires: perl(Moose)
Requires: perl(MooseX::StrictConstructor)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Perl implementation of some of the functionality in Filip Lundborg's dbcli.py and status.py scripts for Dropbox.


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
%doc LICENSE MANIFEST README
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/*

%changelog
* Wed Mar 24 2010 Steve Huff <shuff@vecna.org> - 1.091510-1
- Initial package.
