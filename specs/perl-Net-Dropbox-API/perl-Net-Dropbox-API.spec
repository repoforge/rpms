# $Id$
# Authority: shuff
# Upstream: Lenz Gschwendtner <norbu09$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Dropbox-API

Summary: A Dropbox API interface
Name: perl-Net-Dropbox-API
Version: 1.4
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Dropbox-API/

Source: http://search.cpan.org/CPAN/authors/id/N/NO/NORBU/Net-Dropbox-API-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Data::Random)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTTP::Request::Common)
BuildRequires: perl(JSON)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Mouse)
BuildRequires: perl(Net::OAuth)
BuildRequires: perl(Test::More)
BuildRequires: perl(common::sense)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Data::Random)
Requires: perl(HTTP::Request::Common)
Requires: perl(JSON)
Requires: perl(LWP::UserAgent)
Requires: perl(Mouse)
Requires: perl(Net::OAuth)
Requires: perl(common::sense)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
The Dropbox API is a OAuth based API.

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
%doc Changes META.yml README
%doc examples/
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Net/Dropbox/API.pm
#%{perl_vendorlib}/Net/Dropbox/API/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Thu Apr 28 2011 Steve Huff <shuff@vecna.org> - 1.4-1
- Initial package.
