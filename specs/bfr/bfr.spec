# $Id$
# Authority: dag

Summary: General-purpose command-line pipe buffer
Name: bfr
Version: 1.6
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.glines.org/wiki/bfr

Source: http://www.glines.org/bin/pk/bfr-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Buffer is a general-purpose command-line pipe buffer. It buffers data from
stdin and sends it to stdout, adjusting to best fit the pace stdout can
handle. It can solve problems on either end of a pipe. For instance, if the
incoming stream is slower than outgoing, performance is mainly dependent on
the "start-stream threshold" you set. This can be used to group data into
larger packets to, for an example, reduce seeking on a tape drive. In the
case of the outgoing being slower, the "stop-stream threshold" prevents
unnecessary CPU from being taken up by reading single-bytes and such (if the
output stream accepts data one byte at a time, for instance), and will
output-only until the buffer goes down to 97% or so. This speeds up certain
procedures, such as creating a tar file, gzipping it, and putting it through
a program such as "netcat". It boosts performance by allowing a certain level
of detachment between the two... allowing tar and (especially) gzip to do its
work at the same time the network is doing its work, so you're not sending
one packet and THEN seeing gzip kick in to create the next.

The Buffer distribution also contains a variant of buffer named Bufplay (bfp).
Bufplay's purpose is to do the same sort of buffering as Buffer, but it is
intended for use with OSS, configuring /dev/dsp for the type of sound data
you specify and playing it. If, for some reason, you want to be cool like me
and have 60 megs of RAM inbetween mpg123 and your sound card, you can. =)

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}
										
%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README TODO
%doc %{_mandir}/man1/bfr.1*
%{_bindir}/bfp
%{_bindir}/bfr

%changelog
* Sun Apr 22 2007 Dag Wieers <dag@wieers.com> - 1.6-1
- Initial package. (using DAR)
