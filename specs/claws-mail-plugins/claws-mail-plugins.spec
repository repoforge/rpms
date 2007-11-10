# $Id:$
# Authority: hadams

# define plugin version
%define acpinotifier	1.0.12
%define attremover	1.0.7
%define attachwarner    0.2.8
%define cachesaver	0.10.6
%define fetchinfo	0.4.20
%define gtkhtml2viewer  0.15.2
%define mailmbox	1.14
%define newmail		0.0.11
%define notification	0.12.1
%define pdfviewer       0.6
%define perl		0.9.10
%define rssyl		0.15
%define smime		0.7.2
%define spam_report	0.2
%define synce		0.7.2
%define vcalendar	1.98
Name:           claws-mail-plugins
Version:        3.0.1
Release:        1
Summary:        Additional plugins for claws-mail

Group:          Applications/Internet
License:        GPL
URL:            http://claws-mail.org
Source0:        http://dl.sf.net/sylpheed-claws/claws-mail-extra-plugins-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  claws-mail-devel >= %{version}
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libetpan-devel
BuildRequires:  perl
BuildRequires:  synce-devel
BuildRequires:  curl-devel
BuildRequires:  libxml2-devel
BuildRequires:  gtkhtml2-devel
BuildRequires:  libidn-devel
BuildRequires:  libtool
BuildRequires:  gpgme-devel
BuildRequires:  poppler-devel
BuildRequires:  ghostscript

Requires:       %{name}-acpi-notifier = %{version}-%{release}
Requires:       %{name}-att-remover = %{version}-%{release}
Requires:       %{name}-attachwarner = %{version}-%{release}
Requires:       %{name}-cachesaver = %{version}-%{release}
Obsoletes:      %{name}-etpan-privacy < %{version}-%{release}
Requires:       %{name}-fetchinfo = %{version}-%{release}
Requires:       %{name}-gtkhtml2-viewer = %{version}-%{release}
Obsoletes:      %{name}-maildir < %{version}-%{release}
Requires:       %{name}-mailmbox = %{version}-%{release}
Requires:       %{name}-newmail = %{version}-%{release}
Requires:       %{name}-notification = %{version}-%{release}
Requires:       %{name}-pdfviewer = %{version}-%{release}
Requires:       %{name}-perl = %{version}-%{release}
Requires:       %{name}-rssyl = %{version}-%{release}
Requires:       %{name}-smime = %{version}-%{release}
Requires:       %{name}-synce = %{version}-%{release}
Requires:       %{name}-vcalendar = %{version}-%{release}
# and the ones from main claws-mail-package...
Requires:       %{name}-clamav
Requires:       %{name}-dillo
Requires:       %{name}-spamassassin
Requires:       %{name}-pgp
Requires:       %{name}-bogofilter
Obsoletes:      sylpheed-claws-plugins <= 2.6.0
Provides:       sylpheed-claws-plugins = %{version}-%{release}
Obsoletes:      sylpheed-claws-plugins-etpan-privacy <= 2.6.0
Obsoletes:      sylpheed-claws-plugins-maildir <= 2.6.0

%description
Additional plugins for claws-mail

%package acpi-notifier
Summary:        ACPI notification plugin for claws-mail 
Group:          Applications/Internet
Requires:	claws-mail >= %{version}
Provides:       sylpheed-claws-plugins-acpi-notifier = %{version}-%{release}
Obsoletes:      sylpheed-claws-plugins-acpi-notifier <= 2.6.0

%description acpi-notifier
%{summary}

%package attachwarner
Summary:        attachment warner plugin for claws-mail 
Group:          Applications/Internet
Requires:	claws-mail >= %{version}

%description attachwarner
%{summary}

%package att-remover
Summary:        Attachments remover plugin for claws-mail 
Group:          Applications/Internet
Requires:	claws-mail >= %{version}
Provides:       sylpheed-claws-plugins-att-remover = %{version}-%{release}
Obsoletes:      sylpheed-claws-plugins-att-remover <= 2.6.0

%description att-remover
%{summary}

%package cachesaver
Summary:        A cache saving plugin
Group:          Applications/Internet
Requires:	claws-mail >= %{version}
Provides:       sylpheed-claws-plugins-cachesaver = %{version}-%{release}
Obsoletes:      sylpheed-claws-plugins-cachesaver <= 2.6.0


%description cachesaver
This plugin saves the caches every 60 seconds (or user-defined
period). It helps avoiding the loss of metadata on crashes.

%package fetchinfo
Summary:        Inserts headers containing some download information
Group:          Applications/Internet
Requires:	claws-mail >= %{version}
Provides:       sylpheed-claws-plugins-fetchinfo = %{version}-%{release}
Obsoletes:      sylpheed-claws-plugins-fetchinfo <= 2.6.0

%description fetchinfo
This plugin inserts headers containing some download information:
UIDL, Sylpheeds account name, POP server, user ID and retrieval time.

%package gtkhtml2-viewer
Summary:        GTK Html Viewer
Group:          Applications/Internet
Requires:	claws-mail >= %{version}
Provides:       sylpheed-claws-plugins-gtkhtml2-viewer = %{version}-%{release}
Obsoletes:      sylpheed-claws-plugins-gtkhtml2-viewer <= 2.6.0


%description gtkhtml2-viewer
%{summary}

%package mailmbox
Summary:        Support for mailboxes in mbox format
Group:          Applications/Internet
Requires:	claws-mail >= %{version}
Provides:       sylpheed-claws-plugins-mailmbox = %{version}-%{release}
Obsoletes:      sylpheed-claws-plugins-mailmbox <= 2.6.0


%description mailmbox
This plugin provides direct support for mailboxes in mbox format.

%package newmail
Summary:        Write a msg header summary to a log file
Group:          Applications/Internet
Requires:	claws-mail >= %{version}
Provides:       sylpheed-claws-plugins-newmail = %{version}-%{release}
Obsoletes:      sylpheed-claws-plugins-newmail <= 2.6.0

%description newmail
Write a msg header summary to a log file (defaults to ~/Mail/NewLog) an arrival
of new mail *after* sorting.

%package notification
Summary:        New mail notifications
Group:          Applications/Internet
Requires:	claws-mail >= %{version}
Provides:       sylpheed-claws-plugins-notification = %{version}-%{release}
Obsoletes:      sylpheed-claws-plugins-notification <= 2.6.0

%description notification
This plugin collects various ways to notify the user of new (and possibly unread)
mail. Currently, a popup and a mail banner are implemented.

%package pdfviewer
Summary:        PDF Viewer plugin for claws-mail
Group:          Applications/Internet
Requires:	claws-mail >= %{version}

%description pdfviewer
This plugin enables the viewing of PDF and PostScript attachments using the
Poppler lib.

%package perl
Summary:        Extended filtering engine
Group:          Applications/Internet
Requires:       perl
Requires:	claws-mail >= %{version}
Provides:       sylpheed-claws-plugins-perl = %{version}-%{release}
Obsoletes:      sylpheed-claws-plugins-perl <= 2.6.0

%description perl
This plugin provides an extended filtering engine for the email client
claws-mail. It allows for the use of full perl power in email filters.

%package rssyl
Summary:        RSS plugin for claws-mail
Group:          Applications/Internet
Requires:	claws-mail >= %{version}
Provides:       sylpheed-claws-plugins-rssyl = %{version}-%{release}
Obsoletes:      sylpheed-claws-plugins-rssyl <= 2.6.0

%description rssyl
%{summary}

%package smime
Summary:        S/MIME signed and/or encrypted
Group:          Applications/Internet
Requires:	claws-mail >= %{version}
Provides:       sylpheed-claws-plugins-smime = %{version}-%{release}
Obsoletes:      sylpheed-claws-plugins-smime <= 2.6.0

%description smime
This plugin handles S/MIME signed and/or encrypted mails. You can decrypt
mails, verify signatures or sign and encrypt your own mails.

%package spam_report
Summary:        This plugin reports spam to various places. 
Group:          Applications/Internet
Requires:	claws-mail >= %{version}
Provides:       sylpheed-claws-plugins-spam-report = %{version}-%{release}

%description spam_report
%{summary}

%package synce
Summary:        Keeping the addressbook of a Windows CE device in sync
Group:          Applications/Internet
Requires:	claws-mail >= %{version}
Provides:       sylpheed-claws-plugins-synce = %{version}-%{release}
Obsoletes:      sylpheed-claws-plugins-synce <= 2.6.0

%description synce
This plugin assists in keeping the addressbook of a Windows CE device
(Pocket PC/ iPAQ, Smartphone etc) in sync with Claws' addressbook,
with respect to email addresses.

%package vcalendar
Summary:        vCalendar message handling
Group:          Applications/Internet
Requires:	claws-mail >= %{version}
Provides:       sylpheed-claws-plugins-vcalendar = %{version}-%{release}
Obsoletes:      sylpheed-claws-plugins-vcalendar <= 2.6.0

%description vcalendar
This plugin enables vCalendar message handling like that produced by
Evolution or Outlook.

%prep
%setup -q -n claws-mail-extra-plugins-%{version}

%build
#acpi_notifier
cd acpi_notifier-%{acpinotifier}
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags}

#attachwarner
cd ../attachwarner-%{attachwarner}
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags}

#att_remover
cd ../att_remover-%{attremover}
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags}

# cachesaver
cd ../cachesaver-%{cachesaver}
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags}

#fetchinfo-plugin
cd ../fetchinfo-plugin-%{fetchinfo}
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags}

#gtkhtml2-viewer
cd ../gtkhtml2_viewer-%{gtkhtml2viewer}
%configure --disable-static --disable-dependency-tracking --disable-rpath
%{__make} %{?_smp_mflags} LIBTOOL=%{_bindir}/libtool

#mailmbox
cd ../mailmbox-%{mailmbox}
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags}

#newmail
cd ../newmail-%{newmail}
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags}

#notification-plugin
cd ../notification_plugin-%{notification}
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags}

#pdf viewer
cd ../pdf_viewer-%{pdfviewer}
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags}

#perl
cd ../perl_plugin-%{perl}
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags}

#rssyl
cd ../rssyl-%{rssyl}
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags} LIBTOOL=/usr/bin/libtool

#smime
cd ../smime-%{smime}
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags}

#spam_report
cd ../spam_report-%{spam_report}
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags}

#synce
cd ../synce_plugin-%{synce}
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags}

#vcalendar
cd ../vcalendar-%{vcalendar}
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags} LIBTOOL=/usr/bin/libtool

%install
rm -rf $RPM_BUILD_ROOT

# acpi_notifier
cd acpi_notifier-%{acpinotifier}
%{__make} install DESTDIR=$RPM_BUILD_ROOT CLAWS_MAIL_PLUGINDIR=%{_libdir}/claws-mail/plugins/

# attachwarner
cd ../attachwarner-%{attachwarner}
%{__make} install DESTDIR=$RPM_BUILD_ROOT CLAWS_MAIL_PLUGINDIR=%{_libdir}/claws-mail/plugins/

# att_remover
cd ../att_remover-%{attremover}
%{__make} install DESTDIR=$RPM_BUILD_ROOT CLAWS_MAIL_PLUGINDIR=%{_libdir}/claws-mail/plugins/


# cachesaver
cd ../cachesaver-%{cachesaver}
%{__make} install DESTDIR=$RPM_BUILD_ROOT CLAWS_MAIL_PLUGINDIR=%{_libdir}/claws-mail/plugins/


#fetchinfo-plugin
cd ../fetchinfo-plugin-%{fetchinfo}
%{__make} install DESTDIR=$RPM_BUILD_ROOT CLAWS_MAIL_PLUGINDIR=%{_libdir}/claws-mail/plugins/
 

#gtkhtml2-viewer
cd ../gtkhtml2_viewer-%{gtkhtml2viewer}
%{__make} install DESTDIR=$RPM_BUILD_ROOT CLAWS_MAIL_PLUGINDIR=%{_libdir}/claws-mail/plugins/


#mailmbox
cd ../mailmbox-%{mailmbox}
%{__make} install DESTDIR=$RPM_BUILD_ROOT CLAWS_MAIL_PLUGINDIR=%{_libdir}/claws-mail/plugins/


#newmail
cd ../newmail-%{newmail}
%{__make} install DESTDIR=$RPM_BUILD_ROOT CLAWS_MAIL_PLUGINDIR=%{_libdir}/claws-mail/plugins/


#notification-plugin
cd ../notification_plugin-%{notification}
%{__make} install DESTDIR=$RPM_BUILD_ROOT CLAWS_MAIL_PLUGINDIR=%{_libdir}/claws-mail/plugins/

#pdf viewer
cd ../pdf_viewer-%{pdfviewer}
%{__make} install DESTDIR=$RPM_BUILD_ROOT CLAWS_MAIL_PLUGINDIR=%{_libdir}/claws-mail/plugins/

#perl
cd ../perl_plugin-%{perl}
%{__make} install DESTDIR=$RPM_BUILD_ROOT CLAWS_MAIL_PLUGINDIR=%{_libdir}/claws-mail/plugins/


#rssyl
cd ../rssyl-%{rssyl}
%{__make} install DESTDIR=$RPM_BUILD_ROOT CLAWS_MAIL_PLUGINDIR=%{_libdir}/claws-mail/plugins/


#smime
cd ../smime-%{smime}
%{__make} install DESTDIR=$RPM_BUILD_ROOT CLAWS_MAIL_PLUGINDIR=%{_libdir}/claws-mail/plugins/


#spam_report
cd ../spam_report-%{spam_report}
%{__make} install DESTDIR=$RPM_BUILD_ROOT CLAWS_MAIL_PLUGINDIR=%{_libdir}/claws-mail/plugins/


#synce
cd ../synce_plugin-%{synce}
%{__make} install DESTDIR=$RPM_BUILD_ROOT CLAWS_MAIL_PLUGINDIR=%{_libdir}/claws-mail/plugins/


#vcalendar
cd ../vcalendar-%{vcalendar}
%{__make} install DESTDIR=$RPM_BUILD_ROOT CLAWS_MAIL_PLUGINDIR=%{_libdir}/claws-mail/plugins/


find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
find ${RPM_BUILD_ROOT} -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README

%files acpi-notifier
%defattr(-,root,root,0755)
%doc acpi_notifier-%{acpinotifier}/ChangeLog
%doc acpi_notifier-%{acpinotifier}/COPYING
%doc acpi_notifier-%{acpinotifier}/NEWS
%doc acpi_notifier-%{acpinotifier}/AUTHORS
%doc acpi_notifier-%{acpinotifier}/README
%{_libdir}/claws-mail/plugins/acpi_notifier*
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/acpi_notifier.mo
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/acpi_notifier.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/acpi_notifier.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/acpi_notifier.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/acpi_notifier.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/acpi_notifier.mo
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/acpi_notifier.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/acpi_notifier.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/acpi_notifier.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/acpi_notifier.mo
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/acpi_notifier.mo
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/acpi_notifier.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/acpi_notifier.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/acpi_notifier.mo

%files attachwarner
%defattr(-,root,root,0755)
%{_libdir}/claws-mail/plugins/attachwarner*
%doc attachwarner-%{attachwarner}/AUTHORS
%doc attachwarner-%{attachwarner}/ChangeLog
%doc attachwarner-%{attachwarner}/COPYING
%doc attachwarner-%{attachwarner}/NEWS
%doc attachwarner-%{attachwarner}/README
%doc attachwarner-%{attachwarner}/TODO
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/attachwarner.mo
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/attachwarner.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/attachwarner.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/attachwarner.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/attachwarner.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/attachwarner.mo
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/attachwarner.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/attachwarner.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/attachwarner.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/attachwarner.mo
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/attachwarner.mo
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/attachwarner.mo

%files att-remover
%defattr(-,root,root,0755)
%doc att_remover-%{attremover}/AUTHORS
%doc att_remover-%{attremover}/ChangeLog
%doc att_remover-%{attremover}/COPYING
%doc att_remover-%{attremover}/NEWS
%doc att_remover-%{attremover}/README
%{_libdir}/claws-mail/plugins/att_remover*

%files cachesaver
%defattr(-,root,root,0755)
%doc cachesaver-%{cachesaver}/AUTHORS
%doc cachesaver-%{cachesaver}/ChangeLog
%doc cachesaver-%{cachesaver}/COPYING
%{_libdir}/claws-mail/plugins/cachesaver*

%files fetchinfo
%defattr(-,root,root,0755)
%doc fetchinfo-plugin-%{fetchinfo}/ChangeLog
%doc fetchinfo-plugin-%{fetchinfo}/COPYING
%doc fetchinfo-plugin-%{fetchinfo}/README
%{_libdir}/claws-mail/plugins/fetchinfo*

%files gtkhtml2-viewer
%defattr(-,root,root,0755)
%doc gtkhtml2_viewer-%{gtkhtml2viewer}/AUTHORS
%doc gtkhtml2_viewer-%{gtkhtml2viewer}/COPYING
%{_libdir}/claws-mail/plugins/gtkhtml2_viewer*
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/gtkhtml2_viewer.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/gtkhtml2_viewer.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/gtkhtml2_viewer.mo
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/gtkhtml2_viewer.mo
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/gtkhtml2_viewer.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/gtkhtml2_viewer.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/gtkhtml2_viewer.mo
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/gtkhtml2_viewer.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/gtkhtml2_viewer.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/gtkhtml2_viewer.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/gtkhtml2_viewer.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/gtkhtml2_viewer.mo


%files mailmbox
%defattr(-,root,root,0755)
%doc mailmbox-%{mailmbox}/AUTHORS
%doc mailmbox-%{mailmbox}/ChangeLog
%doc mailmbox-%{mailmbox}/COPYING
%doc mailmbox-%{mailmbox}/README
%{_libdir}/claws-mail/plugins/mailmbox*

%files newmail
%defattr(-,root,root,0755)
%doc newmail-%{newmail}/AUTHORS
%doc newmail-%{newmail}/ChangeLog
%doc newmail-%{newmail}/COPYING
%doc newmail-%{newmail}/NEWS
%doc newmail-%{newmail}/README
%{_libdir}/claws-mail/plugins/newmail.so

%files notification
%defattr(-,root,root,0755)
%doc notification_plugin-%{notification}/AUTHORS
%doc notification_plugin-%{notification}/ChangeLog
%doc notification_plugin-%{notification}/COPYING
%doc notification_plugin-%{notification}/README
%{_libdir}/claws-mail/plugins/notification_plugin.so
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/notification_plugin.mo
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/notification_plugin.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/notification_plugin.mo
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/notification_plugin.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/notification_plugin.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/notification_plugin.mo

%files pdfviewer
%defattr(-,root,root,0755)
%doc pdf_viewer-%{pdfviewer}/AUTHORS
%doc pdf_viewer-%{pdfviewer}/ChangeLog
%doc pdf_viewer-%{pdfviewer}/COPYING
%doc pdf_viewer-%{pdfviewer}/NEWS
%doc pdf_viewer-%{pdfviewer}/README
%{_libdir}/claws-mail/plugins/pdf_viewer.so
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/pdf_viewer.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/pdf_viewer.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/pdf_viewer.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/pdf_viewer.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/pdf_viewer.mo
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/pdf_viewer.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/pdf_viewer.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/pdf_viewer.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/pdf_viewer.mo
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/pdf_viewer.mo
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/pdf_viewer.mo

%files perl
%defattr(-,root,root,0755)
%doc perl_plugin-%{perl}/AUTHORS
%doc perl_plugin-%{perl}/ChangeLog
%doc perl_plugin-%{perl}/COPYING
%doc perl_plugin-%{perl}/README
%doc perl_plugin-%{perl}/sc_perl.pod
%{_libdir}/claws-mail/plugins/perl_plugin.so

%files rssyl
%defattr(-,root,root,0755)
%doc rssyl-%{rssyl}/AUTHORS
%doc rssyl-%{rssyl}/ChangeLog
%doc rssyl-%{rssyl}/COPYING
%doc rssyl-%{rssyl}/TODO
%{_libdir}/claws-mail/plugins/rssyl*
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/rssyl.mo
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/rssyl.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/rssyl.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/rssyl.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/rssyl.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/rssyl.mo
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/rssyl.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/rssyl.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/rssyl.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/rssyl.mo
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/rssyl.mo
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/rssyl.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/rssyl.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/rssyl.mo

%files smime
%defattr(-,root,root,0755)
%doc smime-%{smime}/ChangeLog
%doc smime-%{smime}/COPYING
%doc smime-%{smime}/NEWS
%{_libdir}/claws-mail/plugins/smime*

%files spam_report
%defattr(-,root,root,0755)
%doc spam_report-%{spam_report}/ChangeLog
%doc spam_report-%{spam_report}/COPYING
%doc spam_report-%{spam_report}/NEWS
%{_libdir}/claws-mail/plugins/spamreport*
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/spam_report.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/spam_report.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/spam_report.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/spam_report.mo
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/spam_report.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/spam_report.mo
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/spam_report.mo

%files synce
%defattr(-,root,root,0755)
%doc synce_plugin-%{synce}/AUTHORS
%doc synce_plugin-%{synce}/ChangeLog
%doc synce_plugin-%{synce}/COPYING
%doc synce_plugin-%{synce}/README
%{_libdir}/claws-mail/plugins/synce*

%files vcalendar
%defattr(-,root,root,0755)
%doc vcalendar-%{vcalendar}/AUTHORS
%doc vcalendar-%{vcalendar}/ChangeLog
%doc vcalendar-%{vcalendar}/COPYING
%doc vcalendar-%{vcalendar}/README
%{_libdir}/claws-mail/plugins/vcalendar*
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/vcalendar.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/vcalendar.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/vcalendar.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/vcalendar.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/vcalendar.mo
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/vcalendar.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/vcalendar.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/vcalendar.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/vcalendar.mo
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/vcalendar.mo
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/vcalendar.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/vcalendar.mo
%exclude %{_includedir}/ical.h

%changelog
* Wed Sep 19 2007 Heiko Adams <info@fedora-blog.de>
3.0.1-1
- version upgrade

* Wed Sep 05 2007 Heiko Adams <info@fedora-blog.de>
3.0.0-1
- version upgrade

* Sun Aug 12 2007 Heiko Adams <info@fedora-blog.de>
2.10.0-1
- version upgrade
- rebuild for rpmforge

* Sat Apr 21 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.9.1-1
- version upgrade which fixes pdfviewer bug

* Mon Apr 16 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.9.0-1
- version upgrade

* Tue Mar 06 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.8.0-2
- bump

* Wed Feb 28 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.8.0-1
- version upgrade
- fix rpath

* Wed Feb 07 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.7.1-2
- bump

* Thu Jan 18 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.7.1-1
- version upgrade

* Fri Dec 22 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.6.1-2
- some more fixes

* Mon Dec 11 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.6.1-1
- version upgrade
- rename to claws-mail-plugins

* Thu Nov 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.6.0-1
- version upgrade

* Tue Nov 07 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.5.2-5
- rebuild

* Fri Oct 20 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.5.2-4
- rebuild

* Thu Oct 12 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.5.2-3
- rebuild

* Sun Oct 08 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.5.2-2
- rebuild

* Sat Sep 30 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.5.2-1
- version upgrade

* Tue Sep 26 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.5.0-1
- version upgrade

* Fri Sep 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.4.0-2
- FE6 rebuild

* Wed Aug 02 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.4.0-1
- version upgrade

* Wed Jul 05 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.3.0-2
- bump

* Tue Jun 13 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.3.0-1
- version upgrade

* Tue May 16 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.2.0-1
- version upgrade

* Sat Apr 08 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.1.0-1
- version upgrade

* Fri Feb 17 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.0.0-2
- Rebuild for Fedora Extras 5

* Fri Feb 03 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.0.0-1
- version upgrade

* Sun Dec 25 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.100-2
- rebuild

* Thu Nov 17 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.100-1
- version upgrade

* Sun Aug 21 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.13-5
- enable x86_64 synce plugin

* Sat Aug 20 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.13-4
- add dist tag

* Sat Aug 20 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.13-3
- exlude ical.h

* Thu Aug 18 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.13-2
- use setup macro (-c)
- disable synce build on x86_64 for now (#148003)

* Sun Jul 31 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.9.13-1
- Initial Release
