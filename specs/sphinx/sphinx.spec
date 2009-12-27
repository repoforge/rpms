# $Id$
# Authority: yury
# Upstream:  Sphinx Technologies Inc. <sales$sphinxsearch,com>

Name:           sphinx
Version:        0.9.9
Release:        1%{?dist}
Summary:        Free open-source SQL full-text search engine

Group:          Applications/Text
License:        GPLv2+
URL:            http://sphinxsearch.com
Source0:        http://sphinxsearch.com/downloads/%{name}-%{version}.tar.gz
Source1:        %{name}.init
Patch0:         libsphinxclient-0.9.9.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  mysql-devel
BuildRequires:  postgresql-devel
BuildRequires:  expat-devel
#Requires:

Requires(post): chkconfig
Requires(preun): chkconfig
# This is for /sbin/service
Requires(preun): initscripts


%description
Sphinx is a full-text search engine, distributed under GPL version 2.
Commercial licensing (eg. for embedded use) is also available upon request.

Generally, it's a standalone search engine, meant to provide fast,
size-efficient and relevant full-text search functions to other
applications. Sphinx was specially designed to integrate well with SQL
databases and scripting languages.

Currently built-in data source drivers support fetching data either via
direct connection to MySQL, or PostgreSQL, or from a pipe in a custom XML
format. Adding new drivers (eg. to natively support some other DBMSes) is
designed to be as easy as possible.

Search API is natively ported to PHP, Python, Perl, Ruby, Java, and also
available as a pluggable MySQL storage engine. API is very lightweight so
porting it to new language is known to take a few hours.

As for the name, Sphinx is an acronym which is officially decoded as SQL
Phrase Index. Yes, I know about CMU's Sphinx project.


%package -n libsphinxclient
Summary:        Pure C searchd client API library
Group:          Development/Libraries


%description -n libsphinxclient
Pure C searchd client API library
Sphinx search engine, http://sphinxsearch.com/


%package -n libsphinxclient-devel
Summary:        Development libraries and header files for libsphinxclient
Group:          Development/Libraries
Requires:       libsphinxclient = %{version}-%{release}


%description -n libsphinxclient-devel
Pure C searchd client API library
Sphinx search engine, http://sphinxsearch.com/


%prep
%setup -q
%patch0 -p2 -b .libsphinxclient

# Fix wrong-file-end-of-line-encoding
sed -i 's/\r//' api/ruby/spec/sphinx/sphinx_test.sql
sed -i 's/\r//' api/java/mk.cmd
sed -i 's/\r//' api/ruby/spec/fixtures/keywords.php
sed -i 's/\r//' api/ruby/lib/sphinx/response.rb


%build
%configure --sysconfdir=/etc/sphinx --with-mysql --with-pgsql
make %{?_smp_mflags}

# Build libsphinxclient
cd api/libsphinxclient/
%configure
make #%{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p -c"

# Install sphinx initscript
install -p -D -m 0755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/searchd

# Create /var/log/sphinx
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/sphinx

# Create /var/run/sphinx
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/sphinx

# Create /var/lib/sphinx
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/sphinx

# Create sphinx.conf
cp $RPM_BUILD_ROOT%{_sysconfdir}/sphinx/sphinx-min.conf.dist \
    $RPM_BUILD_ROOT%{_sysconfdir}/sphinx/sphinx.conf
    
# Modify sphinx.conf
sed -i 's/\/var\/log\/searchd.log/\/var\/log\/sphinx\/searchd.log/g' \
$RPM_BUILD_ROOT%{_sysconfdir}/sphinx/sphinx.conf

sed -i 's/\/var\/log\/query.log/\/var\/log\/sphinx\/query.log/g' \
$RPM_BUILD_ROOT%{_sysconfdir}/sphinx/sphinx.conf

sed -i 's/\/var\/log\/searchd.pid/\/var\/run\/sphinx\/searchd.pid/g' \
$RPM_BUILD_ROOT%{_sysconfdir}/sphinx/sphinx.conf

sed -i 's/\/var\/data\/test1/\/var\/lib\/sphinx\/test1/g' \
$RPM_BUILD_ROOT%{_sysconfdir}/sphinx/sphinx.conf

# Create /etc/logrotate.d/sphinx
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
cat > $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/sphinx << EOF
/var/log/sphinx/*.log {
       weekly
       rotate 10
       copytruncate
       delaycompress
       compress
       notifempty
       missingok
}
EOF

# Install libsphinxclient
cd api/libsphinxclient/
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p -c"

# clean-up .la archives
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# clean-up .a archives
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add searchd

%preun
if [ $1 = 0 ] ; then
    /sbin/service searchd stop >/dev/null 2>&1
    /sbin/chkconfig --del searchd
fi


%post -p /sbin/ldconfig -n libsphinxclient


%postun -p /sbin/ldconfig -n libsphinxclient
 


%files
%defattr(-,root,root,-)
%doc COPYING doc/sphinx.txt sphinx-min.conf.dist sphinx.conf.dist example.sql
%dir %{_sysconfdir}/sphinx
%config(noreplace) %{_sysconfdir}/sphinx/sphinx.conf
%exclude %{_sysconfdir}/sphinx/*.conf.dist
%exclude %{_sysconfdir}/sphinx/example.sql
%{_initrddir}/searchd
%config(noreplace) %{_sysconfdir}/logrotate.d/sphinx
%{_bindir}/*
%dir %{_localstatedir}/log/sphinx
%dir %{_localstatedir}/run/sphinx
%dir %{_localstatedir}/lib/sphinx

%files -n libsphinxclient
%defattr(-,root,root,-)
%doc api/java api/ruby api/*.php api/*.py api/libsphinxclient/README
%{_libdir}/libsphinxclient-0*.so


%files -n libsphinxclient-devel
%defattr(-,root,root,-)
%{_libdir}/libsphinxclient.so
%{_includedir}/*

%changelog
* Sun Dec 27 2009 Yury V. Zaytsev <yury@shurup.com> - 0.9.9-1
- Ported over RPMForge from EPEL.
- Bumped to the newest version.
- Patched faulty libsphinxclient.

* Wed Aug 12 2009 Allisson Azevedo <allisson@gmail.com> - 0.9.8.1-3
- Fixed macros consistency.
- Modified make install to keep timestamps.
- Added libsphinxclient package.

* Fri Aug  7 2009 Allisson Azevedo <allisson@gmail.com> - 0.9.8.1-2
- Added sysv init.
- Added logrotate.d entry.

* Thu Jul 30 2009 Allisson Azevedo <allisson@gmail.com> - 0.9.8.1-1
- Initial rpm release.
