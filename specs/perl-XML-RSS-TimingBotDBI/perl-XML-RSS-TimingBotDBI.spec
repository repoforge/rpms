# $Id$

# Authority: dries
# Upstream: Sean M. Burke <sburke$cpan,org>

%define real_name XML-RSS-TimingBotDBI
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: XML::RSS::TimingBot-subclass that saves state with DBI
Name: perl-XML-RSS-TimingBotDBI
Version: 2.01
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-RSS-TimingBotDBI/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/S/SB/SBURKE/XML-RSS-TimingBotDBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This class is for requesting RSS feeds only as often as needed, and
storing in a database the data about how often what feeds can be
requested.

This is a subclass of XML::RSS::TimingBot's methods that stores its data
in a DBI database object that you specify, instead of using
XML::RSS::TimingBot's behavior of storing in a local flat-file database.

To use this class, "use" it, create a new object of this class, and "use
DBI" and make a new database handle-object; then use "rssagent_dbh" to
assign that handle to this TimingBotDBI object; and use
"rssagent_url_field", "rssagent_lastmod_field",
"rssagent_nextupdate_field", and "rssagent_fetag_field" to set up the
right table/field names; and then, finally, you can use the TimingBotDBI
object just like a LWP::UserAgent (actually LWP::UserAgent::Determined)
object, to request RSS feeds.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README ChangeLog
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/RSS/TimingBotDBI.pm
%{perl_vendorlib}/XML/RSS/*.pl
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.01-1
- Initial package.
