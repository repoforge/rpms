# $Id$
# Authority: dries
# Upstream: Sean M. Burke <sburke$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-RSS-TimingBot

Summary: Efficiently fetching RSS feeds
Name: perl-XML-RSS-TimingBot
Version: 2.03
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-RSS-TimingBot/

Source: http://www.cpan.org/modules/by-module/XML/XML-RSS-TimingBot-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
XML::RSS::TimingBot is for requesting RSS feeds only as often as needed.
This class does this in two ways:

* When you request a feed the first time, this class remembers what
Last-Modified and ETag headers it has; that the next time you request
that feed, this class can specify that the feed's server should return
data only if that feed has changed since last time, or has a different
ETag value. If the feed *has* changed, you'll get the HTTP response back
with full content and with a normal "200" status code. If the feed
*hasn't* changed, you'll get a contentless "304" response (meaning "I'm
not giving you any content, because it hasn't changed").

* When you request a feed, this class remembers any data that might be
in the RSS that says how often this feed updates. See XML::RSS::Timing
for the full story; but as a common example if there's a
ttl tag with value 180 in the feed, that means that the feed will rebuild
only once every three hours (180 minutes). When this class sees that in the
received RSS data, it remembers this so that if you go to get the feed
more often than that, it will stop you and give a "304" (Not Modified)
error response.


%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/RSS/TimingBot.*

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.03-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Initial package.
