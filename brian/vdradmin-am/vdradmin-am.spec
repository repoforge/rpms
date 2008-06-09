%define cachedir  %(vdr-config --cachedir  2>/dev/null || echo ERROR)
%define configdir %(vdr-config --configdir 2>/dev/null || echo ERROR)
%define videodir  %(vdr-config --videodir  2>/dev/null || echo ERROR)

Name:           vdradmin-am
Version:        3.5.3
Release:        1%{?dist}
Summary:        Web interface for VDR

Group:          Applications/Internet
License:        GPL
URL:            http://andreas.vdr-developer.org/en/
Source0:        http://andreas.vdr-developer.org/download/%{name}-%{version}.tar.bz2
Source1:        %{name}.init
Source2:        %{name}-httpd.conf
Source3:        %{name}.rwtab
Patch0:         %{name}-3.4.5a-proctitle.patch
Patch1:         %{name}-3.5.3-config.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  vdr-devel >= 1.3.27-0.4
BuildRequires:  gettext
BuildRequires:  perl(Locale::gettext)
Requires:       perl(Locale::gettext)
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd

%description
VDRAdmin-AM is a web interface for managing VDR.  You will need access
to a local or remote VDR install to use this package.


%prep
%setup -q
%patch0
%patch1
%{__perl} -pi -e \
  's|"/video"|"%{videodir}"| ;
   s|^(\$CONFIG\{VDRCONFDIR\}\s*=\s*")[^"]*(.*)|$1%{configdir}$2| ;
   s|\$CONFIG\{VIDEODIR\}/epg\.data|%{cachedir}/epg.data| ;
   s|-s \$AT_FILENAME |-f \$AT_FILENAME|' \
  vdradmind.pl
%{__perl} -pi -e \
  's/vdradmind\.pl/vdradmind/g ; s/(TH vdradmin )1/${1}8/' vdradmind.pl.1
for f in CREDITS HISTORY ; do
  iconv -f iso-8859-1 -t utf-8 $f > $f.utf-8 ; mv $f.utf-8 $f
done
install -pm 644 %{SOURCE2} .


%build
%{__perl} -pe \
  's|^\s*\$CONFFILE\s*=.*|\$CONFFILE = "vdradmind.conf";| ;
   s|^.*COMPILE_DIR.*$|| ;
   s|/usr/share/vdradmin/template|./template|' \
  vdradmind.pl > vdradmind.tmp
%{__perl} ./vdradmind.tmp --config < /dev/null
./make.sh utf8add
./make.sh po


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 vdradmind.pl $RPM_BUILD_ROOT%{_sbindir}/vdradmind
install -Dpm 644 vdradmind.pl.1 $RPM_BUILD_ROOT%{_mandir}/man8/vdradmind.8
install -dm 755 $RPM_BUILD_ROOT/usr/share/vdradmin/epgimages
cp -pR template $RPM_BUILD_ROOT/usr/share/vdradmin
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/locale
cp -pR locale/* $RPM_BUILD_ROOT%{_datadir}/locale
install -Dpm 640 vdradmind.conf $RPM_BUILD_ROOT/var/lib/vdradmin/vdradmind.conf
install -dm 755 $RPM_BUILD_ROOT/var/{cache,log,run}/vdradmin
install -Dpm 755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/vdradmind
chmod 755 $RPM_BUILD_ROOT%{_initrddir}/vdradmind
install -Dpm 644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/rwtab.d/%{name}
%find_lang vdradmin


%clean
rm -rf $RPM_BUILD_ROOT


%pre
%{_sbindir}/groupadd -r vdradmin 2>/dev/null || :
%{_sbindir}/useradd -c "VDR web interface" -d /var/lib/vdradmin \
  -g vdradmin -M -n -r -s /sbin/nologin vdradmin 2>/dev/null || :

%post
/sbin/chkconfig --add vdradmind

%preun
if [ $1 -eq 0 ] ; then
    %{_initrddir}/vdradmind stop >/dev/null || :
    /sbin/chkconfig --del vdradmind
fi

%postun
if [ $1 -gt 0 ] ; then
    rm -rf /var/cache/vdradmin/*
    %{_initrddir}/vdradmind try-restart >/dev/null || :
fi


%files -f vdradmin.lang
%defattr(-,root,root,-)
%doc COPYING CREDITS FAQ HISTORY INSTALL README* contrib/*example convert.pl
%doc %{name}-httpd.conf autotimer2searchtimer.pl
%config(noreplace) %{_sysconfdir}/rwtab.d/%{name}
%{_initrddir}/vdradmind
%{_sbindir}/vdradmind
/usr/share/vdradmin/
%{_mandir}/man8/vdradmind.8*
%defattr(-,vdradmin,vdradmin,-)
%dir /var/cache/vdradmin/
%dir /var/lib/vdradmin/
%config(noreplace) /var/lib/vdradmin/vdradmind.conf
/var/log/vdradmin/
%dir /var/run/vdradmin/


%changelog
* Thu Jan 25 2007 Ville Skyttä <ville.skytta at iki.fi> - 3.5.3-1
- 3.5.3.
- Install UTF-8 locales too.
- Fix default path to EPG images.

* Fri Dec  8 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.5.2-1
- 3.5.2.

* Sat Dec  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.5.1-1
- 3.5.1.
- Add read only root/temporary state config.

* Fri Nov 10 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.5.0-1
- 3.5.0, patch to retain autotimer functionality by default on upgrades.

* Wed Oct 25 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.4.7-3
- Improve description (#211043).

* Tue Oct 17 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.4.7-2
- Move compiled templates to /var/cache/vdradmin, clean them up on upgrades.
- Drop no longer needed Obsoletes and Provides.
- Prune pre-3.4.4 changelog entries.

* Sat Sep 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.4.7-1
- 3.4.7.
- Install optional Apache proxy snippet as doc, not in-place.

* Tue Sep 26 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.4.6-3
- Redirect stdin and stdout to /dev/null in the init script.

* Sun Jul 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.4.6-2
- Improve default config, enable VFAT compatiblity by default.

* Fri Jul 14 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.4.6-1
- 3.4.6.
- Clean up no longer relevant upgrade compat from %%post.

* Thu May 18 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.4.5a-1
- 3.4.5a.

* Fri Apr  7 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.4.4-1
- 3.4.4.

* Thu Mar 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.4.4-0.1.rc
- 3.4.4rc.

* Mon Mar 27 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.4.4-0.1.beta2
- 3.4.4beta2.

* Wed Mar  8 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.4.4-0.1.beta
- 3.4.4beta.
