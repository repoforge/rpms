# $Id$
# Authority: shuff
# Upstream: Max Kanat-Alexander <mkanat$cpan,org>
# ExcludeDist: el3 el4

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Random-Source

Summary: Cryptographically secure, cross-platform replacement for rand()
Name: perl-Crypt-Random-Source
Version: 0.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Random-Source/

Source: http://search.cpan.org/CPAN/authors/id/N/NU/NUFFIN/Crypt-Random-Source-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.008
BuildRequires: perl(Any::Moose) >= 0.11
BuildRequires: perl(Capture::Tiny) >= 0.08
BuildRequires: perl(Carp)
BuildRequires: perl(Errno)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::File)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IO::Select)
BuildRequires: perl(Module::Find)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(bytes)
BuildRequires: perl(namespace::clean) >= 0.08
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.008
Requires: perl(Any::Moose) >= 0.11
Requires: perl(Capture::Tiny) >= 0.08
Requires: perl(Carp)
Requires: perl(Errno)
Requires: perl(ExtUtils::MakeMaker) >= 6.30
Requires: perl(File::Spec)
Requires: perl(IO::File)
Requires: perl(IO::Handle)
Requires: perl(Module::Find)
Requires: perl(Sub::Exporter)
Requires: perl(bytes)
Requires: perl(namespace::clean) >= 0.08

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module provides implementations for a number of byte oriented sources of
random data.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

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
%doc Changes LICENSE META.json README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Crypt/Random/Source.pm
%{perl_vendorlib}/Crypt/Random/Source/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Mon Jan 24 2011 Steve Huff <shuff@vecna.org> - 0.07-1
- Initial package.
