# $Id$
# Authority: dag

### EL5 ships with squirrelmail-1.4.8-5.el5_4.10
### EL4 ships with squirrelmail-1.4.8-5.el4_8.8
### EL3 ships with squirrelmail-1.4.8-16.el3
# ExclusiveDist: el2 el6

Summary: SquirrelMail webmail client
Name: squirrelmail
Version: 1.2.10
Release: 0.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.squirrelmail.org/

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: perl, webserver
Requires: php >= 4.0.4, perl, tmpwatch >= 2.8, aspell, webserver
Requires: /usr/sbin/sendmail

%description
SquirrelMail is a standards-based webmail package written in PHP4. It
includes built-in pure PHP support for the IMAP and SMTP protocols, and
all pages render in pure HTML 4.0 (with no Javascript) for maximum
compatibility across browsers.  It has very few requirements and is very
easy to configure and install. SquirrelMail has all the functionality
you would want from an email client, including strong MIME support,
address books, and folder manipulation.

%prep
%setup
rm -f plugins/make_archive.pl

# Rearrange the documentation
mv AUTHORS ChangeLog COPYING INSTALL README UPGRADE doc/
mv ReleaseNotes doc/ReleaseNotes.txt
mv themes/README.themes doc/
for f in `find plugins -name "README*" -or -name INSTALL \
		   -or -name CHANGES -or -name HISTORY`; do
    mkdir -p doc/`dirname $f`
    mv $f $_
done
mv doc/plugins/squirrelspell/doc/README doc/plugins/squirrelspell
rmdir doc/plugins/squirrelspell/doc
mv plugins/squirrelspell/doc/* doc/plugins/squirrelspell
rm -f doc/plugins/squirrelspell/index.php
rmdir plugins/squirrelspell/doc

# Fixup various files
echo "left_refresh=300" >> data/default_pref
for f in contrib/RPM/squirrelmail.cron contrib/RPM/config.php.rh7; do
    perl -pi -e "s|__ATTDIR__|%{_localstatedir}/spool/squirrelmail/attach/|g;"\
	     -e "s|__PREFSDIR__|%{_localstatedir}/lib/squirrelmail/prefs/|g;" $f
done


%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p -m0755 $RPM_BUILD_ROOT%{_sysconfdir}/squirrelmail
mkdir -p -m0755 $RPM_BUILD_ROOT%{_localstatedir}/lib/squirrelmail/prefs
mkdir -p -m0755 $RPM_BUILD_ROOT%{_localstatedir}/spool/squirrelmail/attach
mkdir -p -m0755 $RPM_BUILD_ROOT%{_datadir}/squirrelmail
mkdir -p -m0755 $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily

# install default_pref
install -m 0644 data/default_pref \
    $RPM_BUILD_ROOT%{_localstatedir}/lib/squirrelmail/prefs

# install the config files
mkdir -p -m0755 $RPM_BUILD_ROOT%{_datadir}/squirrelmail/config
install -m 0644 config/*.php $RPM_BUILD_ROOT%{_datadir}/squirrelmail/config/
install -m 0644 contrib/RPM/config.php.rh7 \
    $RPM_BUILD_ROOT%{_sysconfdir}/squirrelmail/config.php
ln -s ../../../..%{_sysconfdir}/squirrelmail/config.php \
    $RPM_BUILD_ROOT%{_datadir}/squirrelmail/config/config.php
install -m 0755 config/*.pl $RPM_BUILD_ROOT%{_datadir}/squirrelmail/config/

# install index.php
install -m 0644 index.php $RPM_BUILD_ROOT%{_datadir}/squirrelmail/

# install functions
mkdir -p -m0755 $RPM_BUILD_ROOT%{_datadir}/squirrelmail/functions
install -m 0644 functions/* $RPM_BUILD_ROOT%{_datadir}/squirrelmail/functions/

# install src
mkdir -p -m0755 $RPM_BUILD_ROOT%{_datadir}/squirrelmail/src
install -m 0644 src/* $RPM_BUILD_ROOT%{_datadir}/squirrelmail/src/

# install themes
mkdir -p -m0755 $RPM_BUILD_ROOT%{_datadir}/squirrelmail/themes
install -m 0644 themes/*.php $RPM_BUILD_ROOT%{_datadir}/squirrelmail/themes/
mkdir -p -m0755 $RPM_BUILD_ROOT%{_datadir}/squirrelmail/themes/css
install -m 0644 themes/css/*.css \
    $RPM_BUILD_ROOT%{_datadir}/squirrelmail/themes/css/

# install images
mkdir -p -m0755 $RPM_BUILD_ROOT%{_datadir}/squirrelmail/images
install -m 0644 images/* $RPM_BUILD_ROOT%{_datadir}/squirrelmail/images/

# install the plugins
cp -rp plugins $RPM_BUILD_ROOT%{_datadir}/squirrelmail

# install the locales.
cp -rp locale $RPM_BUILD_ROOT%{_datadir}/squirrelmail

# install help files
cp -rp help $RPM_BUILD_ROOT%{_datadir}/squirrelmail

# install the cron script
install -m 0755 contrib/RPM/squirrelmail.cron \
    $RPM_BUILD_ROOT/%{_sysconfdir}/cron.daily/

%if %{rhl7}
# symlink from /var/www/html/webmail to /usr/share/squirrelmail
mkdir -p -m0755 $RPM_BUILD_ROOT/var/www/html
ln -s %{_datadir}/squirrelmail $RPM_BUILD_ROOT/var/www/html/webmail
%else
# install the config file
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -m 644 contrib/RPM/squirrelmail.conf \
	$RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/
%endif


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0755)
%config %dir %{_sysconfdir}/squirrelmail
%config(noreplace) %{_sysconfdir}/squirrelmail/config.php
%if %{rhl7}
  /var/www/html/webmail
%else
  %config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf
%endif
%doc doc/*
%config %{_sysconfdir}/cron.daily/squirrelmail.cron
%dir %{_datadir}/squirrelmail
%dir %{_localstatedir}/lib/squirrelmail
%dir %{_localstatedir}/spool/squirrelmail
%{_datadir}/squirrelmail/config
%{_datadir}/squirrelmail/functions
%{_datadir}/squirrelmail/help
%{_datadir}/squirrelmail/images
%{_datadir}/squirrelmail/locale
%{_datadir}/squirrelmail/plugins
%{_datadir}/squirrelmail/src
%{_datadir}/squirrelmail/themes
%{_datadir}/squirrelmail/index.php
%attr(0700, apache, apache) %dir %{_localstatedir}/lib/squirrelmail/prefs
%attr(0700, apache, apache) %dir %{_localstatedir}/spool/squirrelmail/attach
%{_localstatedir}/lib/squirrelmail/prefs/default_pref

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.10-0.2
- Rebuild for Fedora Core 5.

* Tue Feb 11 2003 Dag Wieers <dag@wieers.com> - 1.2.10-0
- Initial package.
