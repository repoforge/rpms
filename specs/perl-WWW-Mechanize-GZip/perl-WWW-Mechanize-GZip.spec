Name:           perl-WWW-Mechanize-GZip
Version:        0.12
Release:        1%{?dist}
Summary:        Tries to fetch webpages with gzip-compression
License:        CHECK(GPL+ or Artistic)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/WWW-Mechanize-GZip/
Source0:        http://www.cpan.org/modules/by-module/WWW/WWW-Mechanize-GZip-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(WWW::Mechanize)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The WWW::Mechanize::GZip module tries to fetch a URL by requesting gzip-
compression from the webserver.

%prep
%setup -q -n WWW-Mechanize-GZip-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec 05 2011 David Hrbáč <david@hrbac.cz> - 0.12-1
- initial build
