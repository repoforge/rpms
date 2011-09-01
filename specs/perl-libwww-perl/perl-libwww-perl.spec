# $Id$
# Authority: cmr
# Upstream: Gisle Aas <gisle$activestate,com>

### EL6 ships with perl-libwww-perl-5.833-2.el6
### EL5 ships with perl-libwww-perl-5.805-1.1.1
### EL4 ships with perl-libwww-perl-5.79-5
### EL3 ships with perl-libwww-perl-5.65-6
### EL2 ships with perl-libwww-perl-5.53-3
# Tag: rfx

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name libwww-perl

Summary: The World-Wide Web library for Perl
Name: perl-libwww-perl
Version: 5.837
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/libwww-perl/

Source: http://www.cpan.org/authors/id/G/GA/GAAS/libwww-perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Compress::Raw::Zlib)
BuildRequires: perl(Crypt::SSLeay)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Parser) >= 3.33
BuildRequires: perl(IO::Compress::Deflate)
BuildRequires: perl(IO::Compress::Gzip)
BuildRequires: perl(IO::Uncompress::Gunzip)
BuildRequires: perl(IO::Uncompress::Inflate)
BuildRequires: perl(IO::Uncompress::RawInflate)
BuildRequires: perl(MIME::Base64) >= 2.1
BuildRequires: perl(Net::FTP) >= 2.58
BuildRequires: perl(URI) >= 1.10
BuildRequires: perl >= 0:5.006
Requires: perl(Compress::Raw::Zlib)
Requires: perl(Crypt::SSLeay)
Requires: perl(Digest::MD5)
Requires: perl(Encode)
Requires: perl(HTML::Parser) >= 3.33
Requires: perl(IO::Compress::Deflate)
Requires: perl(IO::Compress::Gzip)
Requires: perl(IO::Uncompress::Gunzip)
Requires: perl(IO::Uncompress::Inflate)
Requires: perl(IO::Uncompress::RawInflate)
Requires: perl(MIME::Base64) >= 2.1
Requires: perl(Net::FTP) >= 2.58
Requires: perl(URI) >= 1.10
Requires: perl >= 0:5.006

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description
The World-Wide Web library for Perl.

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
%doc AUTHORS Changes MANIFEST META.yml README README.SSL
%doc %{_mandir}/man3/Bundle::LWP.3pm*
%{_bindir}/lwp-download
%{_bindir}/lwp-dump
%{_bindir}/lwp-mirror
%{_bindir}/lwp-request
%{_bindir}/lwp-rget
%{perl_vendorlib}/Bundle/LWP.pm
%{perl_vendorlib}/File/Listing.pm
%{perl_vendorlib}/HTML/
%{perl_vendorlib}/HTTP/
%{perl_vendorlib}/LWP.pm
%{perl_vendorlib}/LWP/
%{perl_vendorlib}/Net/HTTP.pm
%{perl_vendorlib}/Net/HTTP/
%{perl_vendorlib}/Net/HTTPS.pm
%{perl_vendorlib}/WWW/RobotRules.pm
%{perl_vendorlib}/WWW/RobotRules/AnyDBM_File.pm
%{perl_vendorlib}/lwpcook.pod
%{perl_vendorlib}/lwptut.pod
%{_mandir}/man1/lwp-download.1.gz
%{_mandir}/man1/lwp-dump.1.gz
%{_mandir}/man1/lwp-mirror.1.gz
%{_mandir}/man1/lwp-request.1.gz
%{_mandir}/man1/lwp-rget.1.gz
%{_mandir}/man3/File::Listing.3pm.gz
%{_mandir}/man3/HTML::*.3pm.gz
%{_mandir}/man3/HTTP::*.3pm.gz
%{_mandir}/man3/LWP.3pm.gz
%{_mandir}/man3/LWP::*.3pm.gz
%{_mandir}/man3/Net::HTTP.3pm.gz
%{_mandir}/man3/Net::HTTP::NB.3pm.gz
%{_mandir}/man3/WWW::RobotRules.3pm.gz
%{_mandir}/man3/WWW::RobotRules::AnyDBM_File.3pm.gz
%{_mandir}/man3/lwpcook.3pm.gz
%{_mandir}/man3/lwptut.3pm.gz


%changelog
* Thu Sep 01 2011 Steve Huff <shuff@vecna.org> - 5.837-1
- Updated to version 5.837.
- Move from RFT to RFX.
- Captured dependencies.

* Mon Feb  7 2011 Christoph Maser <cmaser@gmx.de> - 5.835-1
- Updated to version 5.835.

* Thu Jul 23 2009 Christoph Maser <cmr@financial.com> - 5.826-1
- Initial package. (using DAR)
