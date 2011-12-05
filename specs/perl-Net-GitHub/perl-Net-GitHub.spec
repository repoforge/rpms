Name:           perl-Net-GitHub
Version:        0.30
Release:        1%{?dist}
Summary:        Perl Interface for github.com
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Net-GitHub/
Source0:        http://www.cpan.org/modules/by-module/Net/Net-GitHub-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Any::Moose)
BuildRequires:  perl(Crypt::SSLeay)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(JSON::Any)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Test::MockModule)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(WWW::Mechanize::GZip)
Requires:       perl(Any::Moose)
Requires:       perl(Crypt::SSLeay)
Requires:       perl(HTML::TreeBuilder)
Requires:       perl(HTTP::Request::Common)
Requires:       perl(JSON::Any)
Requires:       perl(JSON::XS)
Requires:       perl(URI::Escape)
Requires:       perl(WWW::Mechanize::GZip)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
http://github.com is a popular git host.

%prep
%setup -q -n Net-GitHub-%{version}

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
* Mon Dec 05 2011 David Hrbáč <david@hrbac.cz> - 0.30-1
- initial build
