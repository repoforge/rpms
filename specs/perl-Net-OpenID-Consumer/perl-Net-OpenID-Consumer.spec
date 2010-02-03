# $Id$
# Authority: shuff
# Upstream: Martin Atkins <mart$degeneration,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-OpenID-Consumer

Summary: library for consumers of OpenID identities
Name: perl-%{real_name}
Version: 1.03
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-OpenID-Consumer/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MART/Net-OpenID-Consumer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Crypt::DH) >= 0.05
BuildRequires: perl(Digest::SHA1)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Time::Local)
BuildRequires: perl(URI)
BuildRequires: perl(XML::Simple)
Requires: perl(Crypt::DH) >= 0.05
Requires: perl(Digest::SHA1)
Requires: perl(HTTP::Request)
Requires: perl(LWP::UserAgent)
Requires: perl(MIME::Base64)
Requires: perl(Time::Local)
Requires: perl(URI)
Requires: perl(XML::Simple)

%filter_from_requires /^perl*/d
%filter_setup

%description
This is the Perl API for (the consumer half of) OpenID, a distributed identity
system based on proving you own a URL, which is then your identity. More
information is available at:

  http://openid.net/

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST META.yml
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Net/OpenID/
%{perl_vendorlib}/Net/OpenID/*


%changelog
* Wed Feb 03 2010 Christop Maser <cmr@financial.com> - 1.03-2
- Update dependencies

* Mon Oct 05 2009 Steve Huff <shuff@vecna.org> - 1.03-1
- Initial package.

