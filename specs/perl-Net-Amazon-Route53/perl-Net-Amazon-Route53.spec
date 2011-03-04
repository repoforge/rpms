# $Id$
# Authority: shuff
# Upstream: Marco Fontani <mfontani$cpan,org>
# ExcludeDist: el3 el4

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Amazon-Route53

Summary: Interface to Amazon's Route 53
Name: perl-Net-Amazon-Route53
Version: 0.110310
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Amazon-Route53/

Source: http://search.cpan.org/CPAN/authors/id/M/MF/MFONTANI/Net-Amazon-Route53-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Digest::HMAC_SHA1)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires: perl(FindBin)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Mouse)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Test::More)
BuildRequires: perl(XML::Bare)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Digest::HMAC_SHA1)
Requires: perl(FindBin)
Requires: perl(Getopt::Long)
Requires: perl(HTML::Entities)
Requires: perl(HTTP::Request)
Requires: perl(LWP::UserAgent)
Requires: perl(MIME::Base64)
Requires: perl(Mouse)
Requires: perl(Pod::Usage)
Requires: perl(XML::Bare)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Perl interface to Amazon's Route 53 DNS hosting service.

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
%{_bindir}/*
%{perl_vendorlib}/Net/Amazon/Route53.pm
%{perl_vendorlib}/Net/Amazon/Route53/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Fri Mar 04 2011 Steve Huff <shuff@vecna.org> - 0.110310-1
- Update to version 0.110310.

* Wed Jan 26 2011 Steve Huff <shuff@vecna.org> - 0.110241-1
- Initial package.
