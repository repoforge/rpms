# $Id$
# Authority: shuff
# Upstream: Brad Fitzpatrick <brad$danga,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name LWPx-ParanoidAgent

Summary: subclass of LWP::UserAgent that protects you from harm
Name: perl-%{real_name}
Version: 1.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/LWPx-ParanoidAgent/

Source: http://search.cpan.org/CPAN/authors/id/B/BR/BRADFITZ/LWPx-ParanoidAgent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Net::DNS)
BuildRequires: perl(Time::HiRes)

# we don't want to either provide or require anything from _docdir, per policy
%filter_provides_in %{_docdir}
%filter_requires_in %{_docdir}

# we should not require something we ourselves provide
%filter_from_requires /^perl(LWPx::Protocol::http*/d

# actually set up the filtering
%filter_setup


%description
The LWPx::ParanoidAgent is a class subclassing LWP::UserAgent, but paranoid
against attackers. It's to be used when you're fetching a remote resource on
behalf of a possibly malicious user.

This class can do whatever LWP::UserAgent can (callbacks, uploads from files,
etc), except proxy support is explicitly removed, because in that case you
should do your paranoia at your proxy.

Also, the schemes are limited to http and https, which are mapped to
LWPx::Protocol::http_paranoid and LWPx::Protocol::https_paranoid, respectively,
which are forked versions of the same ones without the "_paranoid". Subclassing
them didn't look possible, as they were essentially just one huge function.

This class protects you from connecting to internal IP ranges (unless you
whitelist them), hostnames/IPs that you blacklist, remote webserver tarpitting
your process (the timeout parameter is changed to be a global timeout over the
entire process), and all combinations of redirects and DNS tricks to otherwise
tarpit and/or connect to internal resources.

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
%doc ChangeLog MANIFEST META.yml
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/LWPx/
%{perl_vendorlib}/LWPx/*

%changelog
* Tue Oct 06 2009 Steve Huff <shuff@vecna.org> - 1.07-1
- Initial package.

